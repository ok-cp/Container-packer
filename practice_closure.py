# Closure 사용 이유
# 서버 프로그래밍 -> 동시성(Concurrency)제어 -> 메모리 공간에 여러 자원이 접근 -> 교착상태(Dead Lock)
# 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 -> Erlang
# 클로저는 공유하되 변경되지 않는(Immutable, Read Only) 적극적으로 사용 -> 함수형 프로그래밍
# 클로저는 불변자료구조 및 atom, STM -> 멀티스레드(Coroutine) 프로그래밍에 강점

# Class - Closure
class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('inner >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)


# Instance
averager_cls = Averager()

# 누적
print(averager_cls(15))
print(averager_cls(35))
print(averager_cls(40))

print()
print()


# Closure - def 
def closure_ex1():
    # Free variable
    series = []
    # closure
    def averager(v):
        # series = [] # 주석 해제 후 확인
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    
    return averager

def closure_ex3():
    n = []
    def action(t):
        n.append(t)
        print(n)
        return n
    return action

avg_closure1 = closure_ex1()

print(avg_closure1(15))
print(avg_closure1(35))
print(avg_closure1(40))

print()
print()

test = closure_ex3()
test(2)
test(3)

# # function inspection

print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print()
print(avg_closure1.__code__.co_freevars)
print()
print(dir(avg_closure1.__closure__[0]))
print()
print(avg_closure1.__closure__[0].cell_contents)

print()
print()


# # 잘못된 클로저 사용
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        cnt += 1 # cnt = cnt + 1
        total += v
        return total / cnt
    
    return averager

avg_closure2 = closure_ex2()

# print(avg_closure2(15)) # 예외


# Nonlocal -> Free variable
def closure_ex4():
    # Free variable
    cnt = 0
    total = 0
    
    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    
    return averager

avg_closure4 = closure_ex4()

print(avg_closure4(15))
print(avg_closure4(35))
print(avg_closure4(40))

