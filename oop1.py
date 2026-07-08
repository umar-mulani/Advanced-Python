class SumOfNumber:


    FIRST =0
    SECOND =0
    def __init__(self,a=12,b=16):
        self.FIRST = a
        self.SECOND = b


    def __del__(self):
        print("object is deleted")


    def main(self):
        print(self.FIRST+self.SECOND)


    def sum(self,a,b):
        print(a+b)


if __name__=="__main__":
    obj = SumOfNumber(20)
    obj.main()

    obj.sum(30,50)
