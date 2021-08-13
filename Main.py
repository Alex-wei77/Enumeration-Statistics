#第一级运算
def gl_cal(res_l):
    global res_list1
    res_list1=[]
    global l1_to_l2
    l1_to_l2=[]
    global ltl_string
    ltl_string=[]
    res_list1 = [m+"＆"+n for m in res_l for n in res_l]
    while (len(l1_to_l2) < len(res_l)):
        l1_to_l2.append("")
    ltl_string= [m+n for m in res_l for n in l1_to_l2]
    for i in res_list1:
        print(i)
    print("共有"+str(len(res_list1))+"种可能")
#第二级运算
def gl_cal2(res_2):
    global res_list2
    res_list2=[]
    res_list2 = [m+"＆"+n for m in ltl_string for n in res_2]
    for i2 in res_list2:
        print(i2)
    print("共有"+str(len(res_list2))+"种可能")
status = True
#用户选择
def continue_choose():
        global status 
        status = True
        user_choose = input("是否继续运行？是请填YES，否请填NO：")
        if user_choose == "YES":
          user_input_2 = input("以空格为间隔连续输入第二次实验中所有等可能的情况：")
          list2 = [n for n in user_input_2.split()]
          gl_cal2(list2)
          print(list2,ltl_string,res_list1,len(l1_to_l2),len(res_list1))
          status = False
        if user_choose == "NO":
          status = False    
        else:
            print("请重新输入！")
            continue_choose()   
#主体
print("欢迎来到两级等可能实验枚举器")
while status == True:
    user_input = input("以空格为间隔连续输入一次实验中所有等可能的情况：")
    list1 = [n for n in user_input.split()]
    gl_cal(list1)
    continue_choose()
      


