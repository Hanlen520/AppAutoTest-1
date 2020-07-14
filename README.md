# **项目名及简介**

## **python3+airtest+poco+unittest 实现移动端自动化测试**

### **目录结构**

#### **1.Base**

**存放公共方法文件**

#### **2.log**

**按天为文件夹存放日志数据，错误截屏图片**

#### **3.PageObject**

**存放PO模式每个页面操作的方法  逻辑层**

#### **4.report**

**存放测试报告**

#### **5.TestCase**

**存放测试用例 控制层**

#### **6.TestData**

**存放测试数据**
**以模块名做文件夹 在写每个用例的yaml文件 根据TestCase目录架构 路径编写**

#### **7.TestSuite**

**存放测试套件 组装测试用例**

### **实现需求**

#### **1.通过TestCase 创建测试用例。**

#### **2.通过TestSuite 组装测试套件。自定义执行多个TestCase**

#### **3.使用airtest 产出html的测试报告 存放在report下html下，并对源码进行重构，产出测试结果**

#### **4.将多份测试报告整合一份测试报告并发送邮件**


### **待实现需求**

#### **1.只能本地查看测试报告**

## **技术文档**

#### 1.unittest.TestSuite()  生成测试套件
    1.先实例化套件
    suite=unittest.TestSuite() (suite：为TestSuite实例化的名称)
    2. 添加某个测试用例的具体测试方法：
    suite.addTest("ClassName(MethodName)")    (ClassName：为类名；MethodName：为方法名)
    3. 添加某个测试用例的所有测试方法
    suite.addTest(unittest.makeSuite(ClassName))  (搜索指定ClassName内test开头的方法并添加到测试套件中)
    4.执行    TestSuite需要配合TextTestRunner才能被执行
    runner=unittest.TextTestRunner()  1. 实例化：(runner：TextTestRunner实例化名称)
    runner.run(suite)           2. 执行： (suite：为测试套件名称)

#### 2.unittest.TestLoader()   用于生成测试套件
    TestCases = unittest.TestLoader().loadTestsFromModule(module)  从模块 py文件 中加载所有测试方法    参数py文件名
    TestCases = unittest.TestLoader().loadTestsFromTestCase(classname)     从类中添加  这个类中的所有的测试方法   参数类名，类必须继承unittest.TestCase
    TestCases = unittest.TestLoader().loadTestsFromName(Name)     加载某个单独的测试方法 必须是字符串   “module.class.def”
    TestCases = unittest.TestLoader().loadTestsFromNames()      加载某个单独的测试方法 必须是列表   [“module.class.def1”,“module.class.def2”]
    suite.addTest(TestCases)
    runner=unittest.Text

