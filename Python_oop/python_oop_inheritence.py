class A:
    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")

class B(A):
    def feature3(self):
     print("This is feature 3")
    
    def feature4(self):
     print("This is feature 4")          

b=B()
b.feature1()

#jokon B A class k inheritence kore tokon single level inheritence bole
#jokon C class B class k and B class A inheritence kore tokon multilevel inheritence bole
#jokon C class ak shate B and A k inheritence kore tokon multiple inheritence bole .but ei khetre B class A k inheritence kore na

#super class subclass ar all feature acces korte parbe na .but subclass super class r all features acces korte parbe