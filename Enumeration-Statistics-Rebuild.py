import configparser,sys
config = configparser.ConfigParser()
# 定义文件路径
path = 'config.ini'
#初始化主体
def mainLoad():
    #运算
    global status
    status = True
    #status标志主体是否继续的
    global ccde
    config.read(path)
    ccde = config['base']['ccde']
    #表示查重功能是否开启
    global last_Part
    last_Part = []
    #last_Part代表上一级事件发生的所有可能
    print("欢迎来到多级等可能实验枚举器")
    while status == True:
        user_input = input("请以空格为间隔连续输入一次实验中所有等可能的情况：")
        list1 = [n for n in user_input.split()]
        gl_cal(list1)
        continue_choose()

def gl_cal(inPut):
#全局标记部分
    global last_Part
    global next_Part
    global calResult
    calResult=[]
    global last_Part_Length
    last_Part_Length=[]

    #如果last_Part为一个空list，则代表第一次运行枚举，即last_part=inPut
    if last_Part == []:
        last_Part = inPut
        while (len(last_Part_Length) < len(last_Part)):
            last_Part_Length.append("")

#输出此次结果
    
    if ccde == 'True':
        for m in last_Part:
            for n in inPut:
                if "("+n+","+m+")" not in calResult and "("+m+","+n+")" not in calResult:
                    calResult.append("("+m+","+n+")")
    elif ccde == "False":
        calResult = ["("+m+","+n+")" for m in last_Part for n in inPut]
    else:
        print("!Wrong Config!")
        sys.exit()

   #将“上一次长度”归零
    last_Part_Length = []
   #原理：将input与last_Part的顺序颠倒，将last_Part换位内容空白长度相同的last_part_Length，以得到这次上下排列结果中后半段输出给下一次作为下一次的“上半段”
    while (len(last_Part_Length) < len(last_Part)):
        last_Part_Length.append("")
    last_Part= [m+n for m in inPut for n in last_Part_Length]



    for i in calResult:
            print(i)
    print("共有"+str(len(calResult))+"种可能")

    

#用户选择
def continue_choose():
        global status 
        status = True
        user_choose = input("是否继续运行？是请填YES，否请填NO：，重置请填写RESTART（全部大小写需统一，全部大写或全部小写）")
        if user_choose == "YES" or user_choose == 'yes':
          user_input_2 = input("请以空格为间隔连续输入第二次实验中所有等可能的情况：")
          list2 = [n for n in user_input_2.split()]
          gl_cal(list2)
          status = continue_choose()
        elif user_choose == "NO" or user_choose == "no":
            status = False
        elif user_choose =="restart" or user_choose == 'RESTART':
            mainLoad()
        else:
            print("请重新输入！")
            continue_choose()   
mainLoad()



      


