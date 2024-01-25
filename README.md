# 백준 문제 푼거 저장소

# 💻기본 파이썬 입력문법
## 📌값(정수형) 입력
```python
N = int(input())
```

## 📌한 줄에 값 여러개 입력
```python
N, M = map(int, input().split())
```

## 📌N값만큼 한줄에 N개의 값 입력
```python
N = int(input())
A = list(map(int, input().strip().split()))[:N]
```

## 📌N값만큼 N줄에 1개씩 값 입력
```python
N = int(input())
M = [int(input()) for _ in range(N)]
```

## 📌여러줄 입력 시 입력 빠르게하기
```python
import sys
input=sys.stdin.readline 
```
