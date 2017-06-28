import unittest
from mydict import Dict

class TestDict(unittest.TestCase):

	def test_init(self):
		d=Dict(a=1,b='test')
		self.assertEqual(d.a,1)  # 断言函数返回的结果与1相等	
		self.assertEqual(d.b,'test')
		self.assertTrue(isinstance(d,dict))
	
	def test_key(self):
		d=Dict()
		d['key']='value'
		self.assertEqual(d.key,'value')
	
	def test_attr(self):
		d=Dict()
		d.key='value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'],'value')
	
	def test_keyerror(self):
		d=Dict()
		with self.assertRaises(KeyError):
			value=d['empty']

	def test_attrerror(self):
		d=Dict()
		with self.assertRaises(AttributeError):
			value=d.empty
#运行单元测试
#一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码：
#if __name__ == '__main__':
 # unittest.main()
#这样就可以把mydict_test.py当做正常的python脚本运行：
#$ python mydict_test.py
#另一种更常见的方法是在命令行通过参数-m unittest直接运行单元测试：
#$ python -m unittest mydict_test

