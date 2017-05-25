# 文件名：实验二死锁避免的模拟.py
# 時間:2017-05-19
# 運行環境:OS X , Python3.6
# 年級:15級
# 班級:4班
# 作者:曹國鴻
# 學號:2015015305


def show(list_f,num):
    if num==1:
        print("""
*****************************************************************************
*\t*资源情况\t*\t   Max   \t*\tAllcation\t*\t  Need  \t*\tAvailable\t* 
*\t   *  \t*             \t*\t         \t*           \t*\t          \t*
*\t进程 *  \t*\tA\tB\tC\t*\tA\tB\tC\t*\tA\tB\tC\t*\tA\tB\tC\t*
*****************************************************************************""")
        for a in list_f:
            print("""*\t  %s  \t*\t%d\t%d\t%d\t*\t%d\t%d\t%d\t*\t%d\t%d\t%d\t*\t          \t*
*****************************************************************************""" % (
                a[0], a[1][0], a[1][1], a[1][2], a[2][0], a[2][1], a[2][2], a[3][0], a[3][1], a[3][2]))
    else:
        lis=[]
        print("""
*********************************************************************************************
*\t*资源情况\t*\t   Work   \t*\t  Need  \t*\tAllocation\t*\t Work+A \t*\t           \t* 
*\t   *  \t*             \t*\t         \t*           \t*\t          \t*\t  Finish  \t*
*\t进程 *  \t*\tA\tB\tC\t*\tA\tB\tC\t*\tA\tB\tC\t*\tA\tB\tC\t*\t           \t*
*********************************************************************************************""")
        for a in list_f:
            try:
                print("""*\t  %s  \t*\t%d\t%d\t%d\t*\t%d\t%d\t%d\t*\t%d\t%d\t%d\t*\t%d\t%d\t%d\t*\t  %s  \t*
*********************************************************************************************""" % (
                    a[0], a[1][0], a[1][1], a[1][2], a[2][0], a[2][1], a[2][2], a[3][0], a[3][1], a[3][2], a[4][0],
                    a[4][1], a[4][2], a[5]))
                lis.append(a[0])
            except:
                print("系统模块错误")
        if lis!=[]:
            print("安全顺序为" + str(lis))

# 銀行家算法檢測是否會產生死鎖
def yhj(list_f,Available,All):
    list_r=[]
    # list_r.append(list_f[0][0]);
    for li in list_f:
        if ge(li[1],All):
            # print("系統處於不安全狀態")
            return list_r,False
    num=0;le=0
    while not list_f==[] and le<len(list_f)+1:
        for li in list_f:
            if ge(Available, li[3]):
                list_r.append([li[0], Available, li[3], li[2], [m + n for m, n in zip(Available, li[2])], True])
                # print(list_r)
                # print(list_f[num])
                Available=[m+n for m,n in zip(Available,li[2])]
                del list_f[num]
                num += 1
            else:
                num+=1;le+=1
        num=0
    return list_r,True





# 比較大小  傳參a(list)，b(list)   返回bool(True,False)
# a(all)>=b(all) or len(a)>len(b)    return True
def ge(list_a,list_b):
    if len(list_a)>len(list_b):
        return True
    elif len(list_b)>len(list_a):
        return False
    else:
        for m, n in zip(list_a,list_b):
            if m >= n:
                continue
            else:
                return False
        return True

#


if __name__=="__main__":
    list_f = [['P0', [7, 5, 3], [0, 1, 0], [7, 4, 3]],
            ['P1', [3, 2, 2], [2, 0, 0], [1, 2, 2]],
            ['P2', [9, 0, 2], [3, 0, 2], [6, 0, 0]],
            ['P3', [2, 2, 2], [2, 1, 1], [0, 1, 1]],
            ['P4', [4, 3, 3], [0, 0, 2], [4, 3, 1]]]
    show(list_f,1)
    Available_str=input("請輸入Available值(用空格分割):").split()
    Available=[]
    for a in Available_str:
        Available.append(int(a))
    All_str=input("請輸入各類資源等總計值(用空格分割):").split()
    All = []
    for a in All_str:
        All.append(int(a))
    lir,bo=yhj(list_f,Available,All)
    # lir, bo = yhj(list_f, [3, 3, 2], [10, 5, 7])
    try:
        if bo:
            show(lir, 2)
        else:
            print("系統處於不安全狀態!!")
    except:
        print("系统未知错误")