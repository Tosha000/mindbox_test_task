# эта функция считает сумму цифр конкретного индекса
def summ(n):
    s=0
    for i in range(n):
        s=s+ n%10
        n=n//10
    return s
def counter(n_customers):
    ID=0
    ID_count={}
    maxn=0
# этот цикл накодит максимальную сумму из указазонного промежутка
    for i in range(n_customers):
        if summ(i)>maxn:
            maxn=summ(i)
# этот цикл заполняет словарь ключами всех возможных сумм из укказанного проемужатка с первоначальным значением 0
    for i in range(maxn+1):
        ID_count[i]=0
# этот цикл считает количесвто покупателей по сумме их индекса, тоесть считает сколько покупателей в каждой группе
    while ID <n_customers:
        s=summ(ID)
        ID_count[s] = ID_count[s] +1
        ID = ID +1
    print(ID_count)
counter(int(input('Введите n_customers: ')))
def counter1(n_customers,n_first_id):
    ID=n_first_id
    ID_count={}
    maxn=0
# этот цикл накодит максимальную сумму из указазонного промежутка
    for i in range(n_first_id, n_first_id + n_customers):
        if summ(i)>maxn:
            maxn=summ(i)
# этот цикл заполняет словарь ключами всех возможных сумм из укказанного проемужатка с первоначальным значением 0
    for i in range(maxn+1):
        ID_count[i]=0
# этот цикл считает количесвто покупателей по сумме их индекса, тоесть считает сколько покупателей в каждой группе
    while ID < n_first_id+ n_customers:
        s=summ(ID)
        ID_count[s] = ID_count[s] +1
        ID = ID +1
# этот цикл удаляет группы, в которых нет ни одного покупателя
    for i in range(len(ID_count)):
        if ID_count[i]==0:
            del ID_count[i]
    print(ID_count)
counter1(int(input('Введите n_customers: ')),int(input('n_first_id: ')))
