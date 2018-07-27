from pymysql import connect

class JD(object):
    def __init__(self):
        self.conn = connect(host= "127.0.0.1",port = 3306, user = "root", 
                            password = "mysql",database = "jing_dong", charset = "utf8")
        self.cursor = self.conn.cursor()        

    def __del__(self):
        self.cursor.close()
        self.conn.close()
    
    def execute_sql(self,sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)
        
    def show_all_items(self):
        sql = "select * from goods;"
        self.execute_sql(sql)

    def show_cates(self):
        sql = "select name from goods_cates;"
        self.execute_sql(sql)

    def show_brands(self):
        sql = "select name from goods_brands;"
        self.execute_sql(sql)

    @staticmethod
    def print_menu():
        print("------京东------")
        print("1.所有的商品")
        print("2.所有商品的分类")
        print("3.所有商品品牌的分类")
        print("q:退出程序")
        num = input("请输入要选择的操作:")
        return num


    def run(self):
        while True:
            num = self.print_menu()
            if num == "1":
                self.show_all_items()
            elif num == "2":
                self.show_cates()
            elif num == "3":
                self.show_brands()
            elif num == "q":
                break
            else:
                print("输入有误,请输入正确的数字....")


def main():
    # 创建一个对象
    jd = JD()
    
    # 调用这个对象中的run方法
    jd.run()

if __name__ == "__main__":
    main()




