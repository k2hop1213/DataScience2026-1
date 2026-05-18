## numpy 정리

1. a.ndim : a가 몇차원 배열인지 출력
2. a.dtype: a의 데이터 타입 출력
3. a.shape: a의 shape를 tuple 형태로 출력
4. np.zeros((2,5)) 0으로 가득찬 배열 생성
5. np.ones((2,5)) 1로 가득 찬거
6. np.full((2,5), data) 어떤 데이터로 채울지 지정해줄 수 있음
7. np.arange(0,10,0.1) step을 지정해줄 수 있고(default는 1) 끝에 값은 포함이 안됨
8. np.linspace(0,10,개수) 범위 사이에 몇개의 값을 만들것인가, 끝에 값이 포함됨
9. np.random.seed(1) seed값을 지정해줄 수 있다. seed값이 같으면 random 한 값을 생성해도 같은 값이 나옴
10. np.random.randint(범위,size = (,),dtype=) 범위사이(끝에 값 포함X)에서 random한 정수가 나옴 (균등분포)
11. np.random.uniform(범위,size(,)) 범위사이(끝에 값 포함X)에서 random한 실수가 나옴 (균등분포)
12. np.random.rand(size) [0,1) 범위사이에 random한 실수 반환(균등분포)
13. np.random.normal(평균,표준편차,size=(,)) 평균과 표준편차를 지정후 random한 실수 반환(정규분포)
14. np.random.randn(size) 평균이 0이고 표준편차가 1인 정규분포 실수
15. slicing은 view를 반환한다
16. fancy indexing, boolean indexing은 copy를 반환한다
17. 브로드캐스팅의 조건
    1. shape가 일치한다
    2. 어느 한 차원의 길이가 같고 한 배열의 다른 차원의 크기가 1이거나 차원이 존재하지 않는다.
18. reshape() reshape 했을때 차원들의 크기를 다 곱하면 원래거랑 똑같아야함
19. 새로운 축을 추가하는법 (np.newaxis,None)
20. sum(), mean(), min(), max(), argmin(), argmax() 는 다차원 배열일때 axis를 지정가능하다 (여러개도 지정가능), 그리고 keepdims = True 를 주게되면 같은 차원의 배열로 반환한다
21. 내적의 조건
    1. 앞 행렬의 열 개수와 뒷 행렬의 행 개수가 같아야함
22. np.sort() 축 지정가능, 정렬된 copy를 반환, a.sort() 는 in-place sorting
23. argsort는 그 자리에 와야하는 index를 반환
