from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer


class ProductListAPIview(APIView):  # 상품 목록 조회
    def get(self, request):  # 상품 목록 조회
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):  # 상품 등록
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # 예외 발생을 true 값으로 둠 -> 유효성 검사 통과하지 못하면 (serializer.errors,status=400) 내부적으로 실행
            serializer.save()  # 유효성 검사 통과하면 products 생성
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # 201=created


class ProductDetailAPIView(APIView):  # 상품 세부 목룍 조회
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk):  # 상품 세부 목록 조회
        products = self.get_object(pk)
        serializer = ProductSerializer(products)
        return Response(serializer.data)

    def put(self, request, pk):  # 상품 수정
        products = self.get_object(pk)
        serializer = ProductSerializer(products, data=request.data, partial=True)
        # partial=True : 부분 수정 가능
        if serializer.is_valid(raise_exception=True):  # 유효성 검사 통과 못하면 error
            serializer.save()
            return Response(serializer.data)  # 수정된 데이터 리턴

    def delete(self, request, pk):  # 상품 삭제
        products = self.get_object(pk)  # 지울 products 조회
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)