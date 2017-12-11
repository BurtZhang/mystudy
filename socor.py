# coding: utf-8 
#!/user/bin/env python3


"""
zucai
"""
__author__ = 'Zhang Hao'

import  re  


#############################
# functions
#############################


def	process01_calc_ph(a,b,c,alpha):
	""" 
	_________________
	"""
	a,b,c,alpha = float(a),float(b),float(c),float(alpha)
	 			
	ph = (1-alpha)/((a*b/(a+b))*c-1)  
	
	return  ph

def	process01_calc(a,b,c,d):
	""" 
	a*b*c/(a+b) = 1+z-e
	d*z = 1-e
	_________________
	z = (a*b*c)/((a+b)*(d+1))
	e = (a+b+a*d+b*d-a*b*c*d)/((a+b)*(d+1))
	x = (b/(a+b))
	y = (a/(a+b))
	"""
	a,b,c,d = float(a),float(b),float(c),float(d)
	 
	x = b/(a+b)
	y = a/(a+b)
	z = (a*b*c)/((a+b)*(d+1))	
	
	e = (a+b+a*d+b*d-a*b*c*d)/((a+b)*(d+1))		
		
	return  (x,y,z,e)
	
def	budan_shengsi_calc(a,b,d1,d2):
	""" 
	y   =(1-alpha)/d1
	a*b = y+z+(1-alpha)
	d2*z=(1-alpha)+y
	"""
	a,b,d1,d2 = float(a),float(b),float(d1),float(d2)
	
	y     = a*b*d2/((1+d1)*(1+d2))
	z 	  = a*b/(1+d2)
	alpha = (d1+d2+d1*d2+a*b*d1*d2+1)/((1+d1)*(1+d2))
	
	return (y,z,alpha)

def	budan_shengsi_calc_ph(a,b,d1,e):
	""" 
	y   =(1-e)/d1
	a*b = y+z+(1-e)
	d2*z=(1-e)+y
	_________________
	a*b = (1-e)/d1+z+(1-e)
	d2*z=(1-e)+(1-e)/d1
	_________________
	z = a*b-(1-e)/d1-(1-e)
	_________________
	d2*(a*b-(1-e)/d1-(1-e)) = (1-e)+(1-e)/d1
	_________________	
	d2 = ((1-e)+(1-e)/d1)/(a*b-(1-e)/d1-(1-e))
	_________________
	"""
	a,b,d1,e = float(a),float(b),float(d1),float(e)
	
	ph = ((1-e)+(1-e)/d1)/(a*b-(1-e)/d1-(1-e))
	
	return  ph

	
def reslut_trans2simp( result_p ):
	""" """
	result_simple = Result_infor_simp()
	
	result_simple.tc_s1_s1    = result_p.tc_result['s1']['s1']  
	result_simple.tc_s1_p1    = result_p.tc_result['s1']['p1']    
	result_simple.tc_s1_f1    = result_p.tc_result['s1']['f1']    
	result_simple.tc_s1_s2    = result_p.tc_result['s1']['s2']    
	result_simple.tc_s1_p2    = result_p.tc_result['s1']['p2']    
	result_simple.tc_s1_f2    = result_p.tc_result['s1']['f2']    
	
	result_simple.tc_p1_s1    = result_p.tc_result['p1']['s1']  
	result_simple.tc_p1_p1    = result_p.tc_result['p1']['p1']    
	result_simple.tc_p1_f1    = result_p.tc_result['p1']['f1']    
	result_simple.tc_p1_s2    = result_p.tc_result['p1']['s2']    
	result_simple.tc_p1_p2    = result_p.tc_result['p1']['p2']    
	result_simple.tc_p1_f2    = result_p.tc_result['p1']['f2']    
	
	result_simple.tc_f1_s1    = result_p.tc_result['f1']['s1']    
	result_simple.tc_f1_p1    = result_p.tc_result['f1']['p1']    
	result_simple.tc_f1_f1    = result_p.tc_result['f1']['f1']    
	result_simple.tc_f1_s2    = result_p.tc_result['f1']['s2']    
	result_simple.tc_f1_p2    = result_p.tc_result['f1']['p2']    
	result_simple.tc_f1_f2    = result_p.tc_result['f1']['f2']    
	
	result_simple.tc_s2_s1    = result_p.tc_result['s2']['s1']   
	result_simple.tc_s2_p1    = result_p.tc_result['s2']['p1']   
	result_simple.tc_s2_f1    = result_p.tc_result['s2']['f1']   
	result_simple.tc_s2_s2    = result_p.tc_result['s2']['s2']   
	result_simple.tc_s2_p2    = result_p.tc_result['s2']['p2']   
	result_simple.tc_s2_f2    = result_p.tc_result['s2']['f2']   
	
	result_simple.tc_p2_s1    = result_p.tc_result['p2']['s1']   
	result_simple.tc_p2_p1    = result_p.tc_result['p2']['p1']   
	result_simple.tc_p2_f1    = result_p.tc_result['p2']['f1']   
	result_simple.tc_p2_s2    = result_p.tc_result['p2']['s2']   
	result_simple.tc_p2_p2    = result_p.tc_result['p2']['p2']   
	result_simple.tc_p2_f2    = result_p.tc_result['p2']['f2']   
	
	result_simple.tc_f2_s1    = result_p.tc_result['f2']['s1']   
	result_simple.tc_f2_p1    = result_p.tc_result['f2']['p1']   
	result_simple.tc_f2_f1    = result_p.tc_result['f2']['f1']   
	result_simple.tc_f2_s2    = result_p.tc_result['f2']['s2']   
	result_simple.tc_f2_p2    = result_p.tc_result['f2']['p2']   
	result_simple.tc_f2_f2    = result_p.tc_result['f2']['f2']   
	
	result_simple.hgy1_s      = result_p.hgy_result1['s']    
	result_simple.hgy1_f      = result_p.hgy_result1['f']      
	
	result_simple.hgy2_s      = result_p.hgy_result2['s']      
	result_simple.hgy2_f      = result_p.hgy_result2['f']      
	
	result_simple.ph11         = result_p.ph11
	result_simple.ph12         = result_p.ph12 
	
	result_simple.ph21         = result_p.ph21
	result_simple.ph22         = result_p.ph22 

	result_simple.ok		  = result_p.ok
	
	return	result_simple
		
def result_trans( func):
	def wrapper( *args,**kw ):		
		return	reslut_trans2simp(func( *args,**kw ))	
	return	wrapper	


def match_infor_trans( match1,match2):
	
	tc1_a = Spf_pan_infor(match1.tc1,(match1.tc1s,match1.tc1p,match1.tc1f),match1.tc1rq)
	tc2_a = Spf_pan_infor(match1.tc2,(match1.tc2s,match1.tc2p,match1.tc2f),match1.tc2rq)
	hgo_a = Spf_pan_infor(match1.hgo,(match1.hgos,match1.hgop,match1.hgof),0)
	hgy_a = Yp_pan_infor(match1.hgy,(match1.hgys,match1.hgyf),match1.hgypkou)
	
	m_infor1 = Match_infor(match1.name,tc1_a,tc2_a,hgy_a,hgo_a)  
	
	tc1_b = Spf_pan_infor(match2.tc1,(match2.tc1s,match2.tc1p,match2.tc1f),match2.tc1rq)
	tc2_b = Spf_pan_infor(match2.tc2,(match2.tc2s,match2.tc2p,match2.tc2f),match2.tc2rq)
	hgo_b = Spf_pan_infor(match2.hgo,(match2.hgos,match2.hgop,match2.hgof),0)
	hgy_b = Yp_pan_infor(match2.hgy,(match2.hgys,match2.hgyf),match2.hgypkou)
	
	m_infor2 = Match_infor(match2.name,tc1_b,tc2_b,hgy_b,hgo_b)  
	
	return     Match_processor(m_infor1,m_infor2)   


###############################################
# class
###############################################



###########################
# class Pan_infor define
# plv  		wr  tuple
# sp  		wr  float
# rangqiu  	ro  float
# water  	wr  tuple
###########################
class	Pan_infor(object):
	"""
# plv  		wr  tuple
# sp  		wr  float
# rangqiu  	ro  float
# water  	wr  tuple	
	"""
	def __init__( self,name ='',plv=list([0,0,0]),pankou=0,sp=1,pn=3):	
		""" """		
		self.__name_set(name)
		self.__pn_set(pn)
		self.__plv_set(plv)
		self.__sp_set(sp)
		self.__pankou_set(pankou)
	
	def __str__( self ):
		""" """	
		return 'Pan_infor object ' + self.__name 
	__repr__ = __str__
	
	def __call__(self):
		""" """
		return 'My name is ' + self.__name 
	
	#################
	#private function	
	##################	
	
	def	_pankou_parse(self,value):  
		""" """   
		if isinstance(value,int):
			if value<9 or value>-9:
			    result	= float(value)
			else:
			    raise ValueError('pankou must be smaller than 9 and bigger than -9!')		
		elif isinstance(value,float):
			temp1 = value%1
			if(temp1 != 0.25 and temp1 != 0.75 and temp1 != 0.5 and temp1 != 0 and abs(value)>=9):    
			    raise ValueError('pankou value error!')	
			else:
			    result	= value       
		elif isinstance(value,str): 
			sr = list()
			sr.append(r'^[\-]?\d{1}$')  
			sr.append(r'^[\-]?\d{1}\.[0]$')  
			sr.append(r'^[\-]?\d{1}\.[0][0]$')  
			sr.append(r'^[\-]?\d{1}\.[5]$')  
			sr.append(r'^[\-]?\d{1}\.[5][0]$') 
			sr.append(r'^[\-]?\d{1}\.[2|7][5]$')       
			
			match_flag = False
			for k in sr:  
			    rl = re.match(k,value)
			    if(rl != None):
			       	result			= float(rl.group(0)) 
			       	match_flag		= True
			       	break 
			if match_flag == False:
			    raise ValueError('pankou str not match!')	
		else:
			raise ValueError('pankou value error!')	
		return result
	
	def _pankousolve( self ):
		""" """
		pankou_abs  = abs(self.__pankou)
		pankou_int	= pankou_abs//1
		pankou_frc  = pankou_abs%1
		if(pankou_frc == 0.75):
			pankou_int +=1
		if(self.__pankou < 0):
			pankou_int = int(0-pankou_int)
			pankou_frc = 1-pankou_frc 
		return [int(pankou_int),pankou_frc]	
	
	def __name_get(self):
		""" """
		return	self.__name
		
	def __name_set(self,name):
		""" """
		self.__name 	= str(name)	
	
	def __pn_get( self ):	
		""" """
		return	self.__pn	
	def __pn_set(self,pn):
		if not (isinstance(pn,int)):
			raise ValueError('pn must be a int!')	
		if(pn<=0):
			raise ValueError('pn must be bigger than 0!')	
		self.__pn 		= pn	
	
	def __sp_get( self ):	
		""" """
		return	self.__sp
	def __sp_set(self,sp):
		if not (isinstance(sp,int) or isinstance(sp,float)):
			raise ValueError('sp must be a int or float!')	
		if(sp<=0):
			raise ValueError('sp must be bigger than 0!')	
		self.__sp 		= sp	
				
	def _plv2water(self,plv ):
		if not (isinstance(plv,list) or isinstance(plv,tuple)):
			raise ValueError('plv must be a list or a tuple!')	
		for k in plv :
			if not (isinstance(k,int) or isinstance(k,float)):
				raise ValueError('plv must be a number!')	
			
		return tuple(map(lambda x: float(x-1),list(plv)))
	
	def _water2plv( self,water ):
		if not (isinstance(water,list) or isinstance(water,tuple)):
			raise ValueError('water must be a list or a tuple!')	
		for k in water :
			if not (isinstance(k,int) or isinstance(k,float)):
				raise ValueError('water must be a number!')	
			
		return tuple(map(lambda x: float(x+1),list(water)))
			
			
	def __plv_get( self ):  
		""" """
		return	tuple(self.__plv)
	
	def	__plv_set( self,value):
		""" """
		if not (isinstance(value,list) or isinstance(value,tuple)):
			raise ValueError('plv must be a list or a tuple!')	
		
		if len(value) != self.__pn_get():
			raise ValueError('plv len must be ' + str(self.pn_get()))	
	
		for k in value :
			if not (isinstance(k,int) or isinstance(k,float)):
				raise ValueError('peilv must be a number!')	
				
		self.__plv 	= tuple(value)
		
	
	def __water_get( self ):
		""" """
		return	tuple(map(lambda x: float(x-1),self.__plv_get()))

	def	__water_set( self,value):
		""" """
		if not isinstance(value,list):
			raise ValueError('water must be a list!')	
		
		if len(value) != self.__pn_get():
			raise ValueError('water len must be %d!' + str(self.__pn_get()))	
			
		for k in value :
			if not (isinstance(k,int) or isinstance(k,float)):
				raise ValueError('water must be a number!')	
					
		self.__plv   = tuple(map(lambda x: float(x+1),value))
			
	#################################
	
	def __pankou_get( self ):
		""" """
		return	self.__pankou	
		
	def __pankou_set( self,value ):
		""" """
		self.__pankou = self._pankou_parse(value)	
	
	def __rangqiu_get( self ):	
		return self._pankousolve()[0]
			
			
	### sp#####
	
	@property
	def sp( self ):
		""" """
		return	self.__sp_get()	
	 
	@property                   
	def name( self ):   
		""" """       
		return	self.__name_get()

	##########################
	## peilv
	##########################	
	
	@property
	def water( self ):
		""" """
		return	self.__water_get()
	@water.setter
	def	water( self,value):
		""" """
		self.__water_set(value)
		
	@property
	def plv( self ):
		""" """
		return	self.__plv_get()
	@plv.setter
	def	plv( self,value):
		""" """
		self.__plv_set(value)
	
	##########################
	## pankou
	##########################
	
	@property
	def pankou( self ):
		""" """
		return	self.__pankou_get()		
	@pankou.setter
	def	pankou( self,value):  
		""" """
		self.__pankou_set(value)
	
	@property
	def rangqiu( self ):
		""" """
		return	self.__rangqiu_get()

		
		
###########################
# class Spf_pan_infor define
# 用来表示胜平负盘信息
###########################
class	Spf_pan_infor(Pan_infor):
	"""
# plv  		wr  tuple
# sp  		wr  float
# rangqiu  	ro  float
# water  	wr  tuple	
	"""	
	#Pan_infor.__init__( self,name ='',plv=[0,0,0],pankou=0,sp=1,pn=3):	
	def __init__( self,name ='',plv=list([0,0,0]),pankou=0):
		""" """
		Pan_infor.__init__(self,name,plv,pankou,1,3)
		
		
		 


###########################
# class Yp_pan_infor define
# 用来表示亚盘信息
###########################
class	Yp_pan_infor(Pan_infor):	
	"""
# plv  		wr  tuple
# sp  		wr  float
# rangqiu  	ro  float
# water  	wr  tuple	
	"""
	#Pan_infor.__init__( self,name ='',plv=[0,0,0],pankou=0,sp=1,pn=3):	
	def __init__( self,name ='',water=[-1,-1],pankou=0):
		""" """
		plv = self._water2plv(water) 
		Pan_infor.__init__(self,name,plv,pankou,1,2)

			 
################################################
# class 			Match_infor
# 比赛信息，把一场比赛的体彩让球不让球，皇冠欧赔压盘放到一起，其中欧盘可选
# tc1表示体彩不让球，tc2表示体彩让求，hgy皇冠亚盘 hgo皇冠欧赔
################################################  
class	Match_infor(dict):
	""" """
	def __init__(self,name,tc1,tc2,hgy,hgo=None):
		""" """
		if not (isinstance(tc1,Spf_pan_infor)):
			raise ValueError('tc1 must be Spf_pan_infor type!')	
		if not (isinstance(tc2,Spf_pan_infor)):
			raise ValueError('tc2 must be Spf_pan_infor type!')	
		if not (isinstance(hgy,Yp_pan_infor)):
			raise ValueError('hgy must be Yp_pan_infor type!')	
		if (not (isinstance(hgo,Spf_pan_infor)) and hgo!= None):
			raise ValueError('hgo must be Spf_pan_infor type or None!')	
		
		self.__name_set(name)
		self.__keys_name   = ('tc1','tc2','hgy','hgo')
			
		if(hgo):
			a = self.__keys_name[:]
			b = (tc1,tc2,hgy,hgo)		
		else:
			a = self.__keys_name[:-1]
			b = (tc1,tc2,hgy)
			
		
		dict.__init__(self,zip(a,b))
			
	def __setitem__( self,key,value ):	
		""" """
		if(key not in self.__keys_name):
			raise ValueError ('key is not ok!')	
		
		if(self.__keys_name[2] == key): 
			if(not isinstance(value,Yp_pan_infor)):
				raise ValueError ('value must be Yp_pan_infor type!')	
		elif(self.__keys_name[3] == key): 
			if (not (isinstance(value,Spf_pan_infor))):
				raise ValueError('hgo must be Spf_pan_infor type!')	
		else: 
			if(not isinstance(value,Spf_pan_infor)):
				raise ValueError ('value must be Spf_pan_infor type!')	
			
		return	dict.__setitem__( self,key,value )
					
	def clear( self ):
		pass
	
	def pop(self):
		pass
		
	def popitem(self):
		pass	
	
	def setdefault(self):
		pass
	
	def update(self):
		pass
	
	#user define	
	def __name_get(self):           
		""" """                     
		return	self.__name         
		                            
	def __name_set(self,name):      
		""" """                     
		self.__name = str(name)	
	
	@property 
	def	match_name(self):
		""" """ 
		return	self.__name_get()
	

################################################
# class 			Result_infor
# 返回二串一投注情况
# tc_result表示体彩投注情况
# s1表示不让球场次的胜，其他依次类推
# 实际上相当于二维数组，第一维表示第一场比赛的投注，一共六种可能
# 第一种六种可能，每种又可能会跟第二场的六种进行组合，所以实际上有36中投注可能
#
# hg_result1 第一场亚盘投注
# hg_result2 第二场亚盘投注
################################################  
class	Result_infor(object):	
	""" """ 
	def __init__( self):  
		""" """ 
		a = ('s1','p1','f1','s2','p2','f2')
		b = (0,0,0,0,0,0)
		c = dict(zip(a,b))
		d = [c.copy(),c.copy(),c.copy(),c.copy(),c.copy(),c.copy()]
		self.__tc_result  = dict(zip(a,d)) 
		self.__hgy_result1 = {'s':0,'f':0}       
		self.__hgy_result2 = {'s':0,'f':0} 
		self.__ph11         = 0
		self.__ph12         = 0 
		self.__ph21         = 0
		self.__ph22         = 0 
		self.__ok           = 0
			
	@property
	def tc_result(self):
		""" """ 
		return    self.__tc_result    
	@tc_result.setter
	def tc_result( self,value ):
		""" """ 
		self.__tc_result  = value
	
	@property
	def hgy_result1(self):
		""" """ 
		return    self.__hgy_result1    
	@hgy_result1.setter
	def hgy_result1( self,value ):
		""" """ 
		self.__hgy_result1  = value
	
	@property
	def hgy_result2(self):
		""" """ 
		return    self.__hgy_result2    
	@hgy_result2.setter
	def hgy_result2( self,value ):
		""" """ 
		self.__hgy_result2  = value
	
	@property
	def ph11(self):
		""" """ 
		return    self.__ph11    
	@ph11.setter
	def ph11( self,value ):
		""" """ 
		self.__ph11  = value
	
	@property
	def ph12(self):
		""" """ 
		return    self.__ph12    
	@ph12.setter
	def ph12( self,value ):
		""" """ 
		self.__ph12  = value
			
	@property
	def ph21(self):
		""" """ 
		return    self.__ph21    
	@ph21.setter
	def ph21( self,value ):
		""" """ 
		self.__ph21  = value
	
	@property
	def ph22(self):
		""" """ 
		return    self.__ph22    
	@ph22.setter
	def ph22( self,value ):
		""" """ 
		self.__ph22  = value

	@property
	def ok(self):
		""" """ 
		return    self.__ok   
	@ok.setter
	def ok( self,value ):
		""" """ 
		self.__ok  = value
	


class	Result_infor_simp(object):
	def	__init__(self):
		self.tc_s1_s1    = 0  
		self.tc_s1_p1    = 0  
		self.tc_s1_f1    = 0  
		self.tc_s1_s2    = 0  
		self.tc_s1_p2    = 0  
		self.tc_s1_f2    = 0  
		
		self.tc_p1_s1    = 0  
		self.tc_p1_p1    = 0  
		self.tc_p1_f1    = 0  
		self.tc_p1_s2    = 0  
		self.tc_p1_p2    = 0  
		self.tc_p1_f2    = 0  
		
		self.tc_f1_s1    = 0  
		self.tc_f1_p1    = 0  
		self.tc_f1_f1    = 0  
		self.tc_f1_s2    = 0  
		self.tc_f1_p2    = 0  
		self.tc_f1_f2    = 0  
		
		self.tc_s2_s1    = 0  
		self.tc_s2_p1    = 0  
		self.tc_s2_f1    = 0  
		self.tc_s2_s2    = 0  
		self.tc_s2_p2    = 0  
		self.tc_s2_f2    = 0  
		
		self.tc_p2_s1    = 0  
		self.tc_p2_p1    = 0  
		self.tc_p2_f1    = 0  
		self.tc_p2_s2    = 0  
		self.tc_p2_p2    = 0  
		self.tc_p2_f2    = 0  
		
		self.tc_f2_s1    = 0  
		self.tc_f2_p1    = 0  
		self.tc_f2_f1    = 0  
		self.tc_f2_s2    = 0  
		self.tc_f2_p2    = 0  
		self.tc_f2_f2    = 0  
		
		self.hgy1_s      = 0    
		self.hgy1_f      = 0     
	
		self.hgy2_s      = 0     
		self.hgy2_f      = 0     
		
		self.ph11         = 0
		self.ph12         = 0 
		self.ph21         = 0
		self.ph22         = 0 

		self.ok          = 0 
		

		
################################################
# class 			Match_processor
################################################  

class	Match_processor(object):	
	""" """ 
	def __init__( self,match1,match2):
		self.__match1_set(match1)
		self.__match2_set(match2)
		self.__processor = {}
		self.__processor['1'] = self.cs_process01  ;
		
	def __match1_get( self):
		return	self.__match1 
		
	def __match1_set( self,match ):
		if not isinstance(match,Match_infor):
			raise ValueError('match must be Match_infor type!')	
		self.__match1 = match	
	
	def __match2_get( self):
		return	self.__match2 
		
	def __match2_set( self,match ):
		if not isinstance(match,Match_infor):
			raise ValueError('match must be Match_infor type!')	
		self.__match2 = match	
	
	def  process01(self,alpha=0.08,t_tou = 10000):
		
		match1 = self.__match1_get()   
		match2 = self.__match2_get()         
		result = Result_infor()  
		
		pan1_sub  = match1['tc1'].pankou-match1['tc2'].pankou      
		pan21_sub  = match2['tc1'].pankou-match2['hgy'].pankou    
		pan22_sub  = match2['tc2'].pankou-match2['hgy'].pankou    
		
		rel_list 	= list()  
		ph_sub  	= 100
		ph      	= 100
		x,y,z,e     = 0,0,0,0
		
		#1
		if (pan1_sub >=0.5 and pan21_sub >=0.5):
			a  = match1['tc1'].plv[0] 
			b  = match1['tc2'].plv[2]	
			c  = match2['tc1'].plv[0]	
			d = match2['hgy'].water[1]
			
			ph = process01_calc_ph(a,b,c,alpha)
			ph_sub  = ph - d
			if(ph_sub <= 0):
				x,y,z,e = process01_calc(a,b,c,d)
			else:
				x,y,z,e = 0,0,0,0
			rel_list.append((1,ph,ph_sub,x,y,z,e))
		
		#2
		if (pan1_sub >=0.5 and pan21_sub <=-0.5):
			a  = match1['tc1'].plv[0] 
			b  = match1['tc2'].plv[2]	
			c  = match2['tc1'].plv[2]	
			d = match2['hgy'].water[0]
			
			ph = process01_calc_ph(a,b,c,alpha)
			ph_sub  = ph - d
			if(ph_sub <= 0):
				x,y,z,e = process01_calc(a,b,c,d)
			else:
				x,y,z,e = 0,0,0,0
			rel_list.append((2,ph,ph_sub,x,y,z,e))
		
		#3
		if (pan1_sub >=0.5 and pan22_sub >=0.5):
			a  = match1['tc1'].plv[0] 
			b  = match1['tc2'].plv[2]	
			c  = match2['tc2'].plv[0]	
			d = match2['hgy'].water[1]
			
			ph = process01_calc_ph(a,b,c,alpha)
			ph_sub  = ph - d
			if(ph_sub <= 0):
				x,y,z,e = process01_calc(a,b,c,d)
			else:
				x,y,z,e = 0,0,0,0
			rel_list.append((3,ph,ph_sub,x,y,z,e))
		
		#4
		if (pan1_sub >=0.5 and pan22_sub <=-0.5):
			a  = match1['tc1'].plv[0] 
			b  = match1['tc2'].plv[2]	
			c  = match2['tc2'].plv[2]	
			d = match2['hgy'].water[0]
			
			ph = process01_calc_ph(a,b,c,alpha)
			ph_sub  = ph - d
			if(ph_sub <= 0):
				x,y,z,e = process01_calc(a,b,c,d)
			else:
				x,y,z,e = 0,0,0,0
			rel_list.append((4,ph,ph_sub,x,y,z,e))
		
		#5
		if (pan1_sub <=-0.5 and pan21_sub >=0.5):
			a  = match1['tc1'].plv[2] 
			b  = match1['tc2'].plv[0]	
			c  = match2['tc1'].plv[0]	
			d = match2['hgy'].water[1]
			
			ph = process01_calc_ph(a,b,c,alpha)
			ph_sub  = ph - d
			if(ph_sub <= 0):
				x,y,z,e = process01_calc(a,b,c,d)
			else:
				x,y,z,e = 0,0,0,0
			rel_list.append((5,ph,ph_sub,x,y,z,e))
		
		#6
		if (pan1_sub <=-0.5 and pan21_sub <=-0.5):
			a  = match1['tc1'].plv[2] 
			b  = match1['tc2'].plv[0]	
			c  = match2['tc1'].plv[2]	
			d = match2['hgy'].water[0]
			
			ph = process01_calc_ph(a,b,c,alpha)
			ph_sub  = ph - d
			if(ph_sub <= 0):
				x,y,z,e = process01_calc(a,b,c,d)
			else:
				x,y,z,e = 0,0,0,0
			rel_list.append((6,ph,ph_sub,x,y,z,e))
		
		#7
		if (pan1_sub <= -0.5 and pan22_sub >=0.5):
			a  = match1['tc1'].plv[2] 
			b  = match1['tc2'].plv[0]	
			c  = match2['tc2'].plv[0]	
			d = match2['hgy'].water[1]
			
			ph = process01_calc_ph(a,b,c,alpha)
			ph_sub  = ph - d
			if(ph_sub <= 0):
				x,y,z,e = process01_calc(a,b,c,d)
			else:
				x,y,z,e = 0,0,0,0
			rel_list.append((7,ph,ph_sub,x,y,z,e))
		
		#8
		if (pan1_sub <= -0.5 and pan22_sub <=-0.5):
			a  = match1['tc1'].plv[2] 
			b  = match1['tc2'].plv[0]	
			c  = match2['tc2'].plv[2]	
			d = match2['hgy'].water[0]
			
			ph = process01_calc_ph(a,b,c,alpha)
			ph_sub  = ph - d
			if(ph_sub <= 0):
				x,y,z,e = process01_calc(a,b,c,d)
			else:
				x,y,z,e = 0,0,0,0
			rel_list.append((8,ph,ph_sub,x,y,z,e))
		
		rel_list_sorted = list(filter(lambda x:x[1]>0,rel_list))	
		rel_list_sorted.sort(key = lambda x:x[2])
		if len(rel_list_sorted)	!= 0 :
			rel = rel_list_sorted[0]
			if(rel[0] == 1):
				result.ph22 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['s1']['s1'] = round(rel[3]*t_tou)  
					result.tc_result['f2']['s1'] = round(rel[4]*t_tou)  
					result.hgy_result2['f'] 	 = round(rel[5]*t_tou)
			elif(rel[0] == 2):
				result.ph21 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['s1']['f1'] = round(rel[3]*t_tou)  
					result.tc_result['f2']['f1'] = round(rel[4]*t_tou)  
					result.hgy_result2['s'] 	 = round(rel[5]*t_tou)
			elif(rel[0] == 3):
				result.ph22 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['s1']['s2'] = round(rel[3]*t_tou)  
					result.tc_result['f2']['s2'] = round(rel[4]*t_tou)  
					result.hgy_result2['f'] 	 = round(rel[5]*t_tou)
			elif(rel[0] == 4):
				result.ph21 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['s1']['f2'] = round(rel[3]*t_tou)  
					result.tc_result['f2']['f2'] = round(rel[4]*t_tou)  
					result.hgy_result2['s'] 	 = round(rel[5]*t_tou)
			elif(rel[0] == 5):
				result.ph22 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['f1']['s1'] = round(rel[3]*t_tou)  
					result.tc_result['s2']['s1'] = round(rel[4]*t_tou)  
					result.hgy_result2['f'] 	 = round(rel[5]*t_tou)
			elif(rel[0] == 6):
				result.ph21 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['f1']['f1'] = round(rel[3]*t_tou)  
					result.tc_result['s2']['f1'] = round(rel[4]*t_tou)  
					result.hgy_result2['s'] 	 = round(rel[5]*t_tou)
			elif(rel[0] == 7):
				result.ph22 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['f1']['s2'] = round(rel[3]*t_tou)  
					result.tc_result['s2']['s2'] = round(rel[4]*t_tou)  
					result.hgy_result2['f'] 	 = round(rel[5]*t_tou)
			elif(rel[0] == 8):
				result.ph21 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['f1']['f2'] = round(rel[3]*t_tou)  
					result.tc_result['s2']['f2'] = round(rel[4]*t_tou)  
					result.hgy_result2['s'] 	 = round(rel[5]*t_tou)	
			else:
				pass
		else:
			pass
			
		return    result
	
	def  process02(self,alpha=0.08,t_tou = 10000):
		
		match1 = self.__match1_get()   
		match2 = self.__match2_get()         
		result = Result_infor()  
		
		pan11_sub  = match1['tc1'].pankou-match1['hgy'].pankou      
		pan12_sub  = match1['tc2'].pankou-match1['hgy'].pankou    
		
		pan21_sub  = match2['tc1'].pankou-match2['hgy'].pankou    
		pan22_sub  = match2['tc2'].pankou-match2['hgy'].pankou    
		
		rel_list = list()  
		ph_sub  = 100
		ph      = 100
		y,z,e   = 0,0,0
		

		#1
		if (pan11_sub >=0.5 and pan21_sub >=0.5):
			a1  = match1['tc1'].plv[0] 
			d1 = match1['hgy'].water[1]		
			a2  = match2['tc1'].plv[0]	
			d2 = match2['hgy'].water[1]
			
			ph = budan_shengsi_calc_ph(a1,a2,d1,alpha)	
			ph_sub  = ph - d2
			if(ph_sub<=0):			
				y,z,e = budan_shengsi_calc(a1,a2,d1,d2)
			else:
				y,z,e = 0,0,0
				rel_list.append((1,ph,ph_sub,y,z,e))
				
		#2
		if (pan11_sub >=0.5 and pan21_sub <=-0.5):
			a1  = match1['tc1'].plv[0] 
			d1 = match1['hgy'].water[1]	
			a2  = match2['tc1'].plv[2]	
			d2 = match2['hgy'].water[0]
		
			ph = budan_shengsi_calc_ph(a1,a2,d1,alpha)	
			ph_sub  = ph - d2
			if(ph_sub<=0):			
				y,z,e = budan_shengsi_calc(a1,a2,d1,d2)
			else:
				y,z,e = 0,0,0
			rel_list.append((2,ph,ph_sub,y,z,e))
		#3
		if (pan11_sub <=-0.5 and pan21_sub >=0.5):
			a1  = match1['tc1'].plv[2] 
			d1 = match1['hgy'].water[0]	
			a2  = match2['tc1'].plv[0]	
			d2 = match2['hgy'].water[1]
			
			ph = budan_shengsi_calc_ph(a1,a2,d1,alpha)	
			ph_sub  = ph - d2
			if(ph_sub<=0):			
				y,z,e = budan_shengsi_calc(a1,a2,d1,d2)
			else:
				y,z,e = 0,0,0
			rel_list.append((3,ph,ph_sub,y,z,e))	
		#4
		if (pan11_sub <=-0.5 and pan21_sub <=-0.5):
			a1  = match1['tc1'].plv[2] 
			d1 = match1['hgy'].water[0]	
			a2  = match2['tc1'].plv[2]	
			d2 = match2['hgy'].water[0]
			
			ph = budan_shengsi_calc_ph(a1,a2,d1,alpha)	
			ph_sub  = ph - d2
			if(ph_sub<=0):			
				y,z,e = budan_shengsi_calc(a1,a2,d1,d2)
			else:
				y,z,e = 0,0,0
			rel_list.append((4,ph,ph_sub,y,z,e))	
		
		#5
		if (pan11_sub >=0.5 and pan22_sub >=0.5):
			a1  = match1['tc1'].plv[0] 
			d1 = match1['hgy'].water[1]
			
			a2  = match2['tc2'].plv[0]	
			d2 = match2['hgy'].water[1]
			
			ph = budan_shengsi_calc_ph(a1,a2,d1,alpha)	
			ph_sub  = ph - d2
			if(ph_sub<=0):			
				y,z,e = budan_shengsi_calc(a1,a2,d1,d2)
			else:
				y,z,e = 0,0,0
			rel_list.append((5,ph,ph_sub,y,z,e))
		#6
		if (pan11_sub >=0.5 and pan22_sub <=-0.5):
			a1  = match1['tc1'].plv[0] 
			d1 = match1['hgy'].water[1]	
			a2  = match2['tc2'].plv[2]	
			d2 = match2['hgy'].water[0]
		
			ph = budan_shengsi_calc_ph(a1,a2,d1,alpha)	
			ph_sub  = ph - d2
			if(ph_sub<=0):			
				y,z,e = budan_shengsi_calc(a1,a2,d1,d2)
			else:
				y,z,e = 0,0,0
			rel_list.append((6,ph,ph_sub,y,z,e))
		#7
		if (pan11_sub <=-0.5 and pan22_sub >=0.5):
			a1  = match1['tc1'].plv[2] 
			d1 = match1['hgy'].water[0]	
			a2  = match2['tc2'].plv[0]	
			d2 = match2['hgy'].water[1]
			
			ph = budan_shengsi_calc_ph(a1,a2,d1,alpha)	
			ph_sub  = ph - d2
			if(ph_sub<=0):			
				y,z,e = budan_shengsi_calc(a1,a2,d1,d2)
			else:
				y,z,e = 0,0,0
			rel_list.append((7,ph,ph_sub,y,z,e))	
		#8
		if (pan11_sub <=-0.5 and pan22_sub <=-0.5):
			a1  = match1['tc1'].plv[2] 
			d1 = match1['hgy'].water[0]	
			a2  = match2['tc2'].plv[2]	
			d2 = match2['hgy'].water[0]
			
			ph = budan_shengsi_calc_ph(a1,a2,d1,alpha)	
			ph_sub  = ph - d2
			if(ph_sub<=0):			
				y,z,e = budan_shengsi_calc(a1,a2,d1,d2)
			else:
				y,z,e = 0,0,0
			rel_list.append((8,ph,ph_sub,y,z,e))	
		
		#9
		if (pan12_sub >=0.5 and pan21_sub >=0.5):
			a1  = match1['tc2'].plv[0] 
			d1 = match1['hgy'].water[1]		
			a2  = match2['tc1'].plv[0]	
			d2 = match2['hgy'].water[1]
			
			ph = budan_shengsi_calc_ph(a1,a2,d1,alpha)	
			ph_sub  = ph - d2
			if(ph_sub<=0):			
				y,z,e = budan_shengsi_calc(a1,a2,d1,d2)
			else:
				y,z,e = 0,0,0
			rel_list.append((9,ph,ph_sub,y,z,e))
				
		#10
		if (pan12_sub >=0.5 and pan21_sub <=-0.5):
			a1  = match1['tc2'].plv[0] 
			d1 = match1['hgy'].water[1]	
			a2  = match2['tc1'].plv[2]	
			d2 = match2['hgy'].water[0]
		
			ph = budan_shengsi_calc_ph(a1,a2,d1,alpha)	
			ph_sub  = ph - d2
			if(ph_sub<=0):			
				y,z,e = budan_shengsi_calc(a1,a2,d1,d2)
			else:
				y,z,e = 0,0,0
			rel_list.append((10,ph,ph_sub,y,z,e))
		#11
		if (pan12_sub <=-0.5 and pan21_sub >=0.5):
			a1  = match1['tc2'].plv[2] 
			d1 = match1['hgy'].water[0]	
			a2  = match2['tc1'].plv[0]	
			d2 = match2['hgy'].water[1]
			
			ph = budan_shengsi_calc_ph(a1,a2,d1,alpha)	
			ph_sub  = ph - d2
			if(ph_sub<=0):			
				y,z,e = budan_shengsi_calc(a1,a2,d1,d2)
			else:
				y,z,e = 0,0,0
			rel_list.append((11,ph,ph_sub,y,z,e))	
		#12
		if (pan12_sub <=-0.5 and pan21_sub <=-0.5):
			a1  = match1['tc2'].plv[2] 
			d1 = match1['hgy'].water[0]	
			a2  = match2['tc1'].plv[2]	
			d2 = match2['hgy'].water[0]
			
			ph = budan_shengsi_calc_ph(a1,a2,d1,alpha)	
			ph_sub  = ph - d2
			if(ph_sub<=0):			
				y,z,e = budan_shengsi_calc(a1,a2,d1,d2)
			else:
				y,z,e = 0,0,0
			rel_list.append((12,ph,ph_sub,y,z,e))	
		
		#13
		if (pan12_sub >=0.5 and pan22_sub >=0.5):
			a1  = match1['tc2'].plv[0] 
			d1 = match1['hgy'].water[1]
			
			a2  = match2['tc2'].plv[0]	
			d2 = match2['hgy'].water[1]
			
			ph = budan_shengsi_calc_ph(a1,a2,d1,alpha)	
			ph_sub  = ph - d2
			if(ph_sub<=0):			
				y,z,e = budan_shengsi_calc(a1,a2,d1,d2)
			else:
				y,z,e = 0,0,0
			rel_list.append((13,ph,ph_sub,y,z,e))
		#14
		if (pan12_sub >=0.5 and pan22_sub <=-0.5):
			a1  = match1['tc2'].plv[0] 
			d1 = match1['hgy'].water[1]	
			a2  = match2['tc2'].plv[2]	
			d2 = match2['hgy'].water[0]
		
			ph = budan_shengsi_calc_ph(a1,a2,d1,alpha)	
			ph_sub  = ph - d2
			if(ph_sub<=0):			
				y,z,e = budan_shengsi_calc(a1,a2,d1,d2)
			else:
				y,z,e = 0,0,0
			rel_list.append((14,ph,ph_sub,y,z,e))
		#15
		if (pan12_sub <=-0.5 and pan22_sub >=0.5):
			a1  = match1['tc2'].plv[2] 
			d1 = match1['hgy'].water[0]	
			a2  = match2['tc2'].plv[0]	
			d2 = match2['hgy'].water[1]
			
			ph = budan_shengsi_calc_ph(a1,a2,d1,alpha)	
			ph_sub  = ph - d2
			if(ph_sub<=0):			
				y,z,e = budan_shengsi_calc(a1,a2,d1,d2)
			else:
				y,z,e = 0,0,0
			rel_list.append((15,ph,ph_sub,y,z,e))	
		#16		
		if (pan12_sub <=-0.5 and pan22_sub <=-0.5):
			
			a1  = match1['tc2'].plv[2] 
			d1 = match1['hgy'].water[0]	
			a2  = match2['tc2'].plv[2]	
			d2 = match2['hgy'].water[0]
			
			ph = budan_shengsi_calc_ph(a1,a2,d1,alpha)	
			ph_sub  = ph - d2
			if(ph_sub<=0):			
				y,z,e = budan_shengsi_calc(a1,a2,d1,d2)
			else:
				y,z,e = 0,0,0
			rel_list.append((16,ph,ph_sub,y,z,e))			
		
		rel_list_sorted = list(filter(lambda x:x[1]>0,rel_list))	
		rel_list_sorted.sort(key = lambda x:x[2])

		if len(rel_list_sorted)	!= 0 :
			rel = rel_list_sorted[0]
			if(rel[0] == 1):
				result.ph22 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['s1']['s1'] = t_tou  
					result.hgy_result1['f'] 	 = round(rel[3]*t_tou)
					result.hgy_result2['f'] 	 = round(rel[4]*t_tou)
			elif(rel[0] == 2):
				result.ph21 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['s1']['f1'] = t_tou  
					result.hgy_result1['f'] 	 = round(rel[3]*t_tou)   
					result.hgy_result2['s'] 	 = round(rel[4]*t_tou)   
			elif(rel[0] == 3):
				result.ph22 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['f1']['s1'] = t_tou  
					result.hgy_result1['s'] 	 = round(rel[3]*t_tou)   
					result.hgy_result2['f'] 	 = round(rel[4]*t_tou)   
			elif(rel[0] == 4):
				result.ph21 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['f1']['f1'] = t_tou  
					result.hgy_result1['s'] 	 = round(rel[3]*t_tou)   
					result.hgy_result2['s'] 	 = round(rel[4]*t_tou)   
			elif(rel[0] == 5):
				result.ph22 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['s1']['s2'] = t_tou  
					result.hgy_result1['f'] 	 = round(rel[3]*t_tou)   
					result.hgy_result2['f'] 	 = round(rel[4]*t_tou)   
			elif(rel[0] == 6):
				result.ph21 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['s1']['f2'] = t_tou  
					result.hgy_result1['f'] 	 = round(rel[3]*t_tou)   
					result.hgy_result2['s'] 	 = round(rel[4]*t_tou)   
			elif(rel[0] == 7):
				result.ph22 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['f1']['s2'] = t_tou  
					result.hgy_result1['s'] 	 = round(rel[3]*t_tou)   
					result.hgy_result2['f'] 	 = round(rel[4]*t_tou)   
			elif(rel[0] == 8):
				result.ph21 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['f1']['f2'] = t_tou  
					result.hgy_result1['s'] 	 = round(rel[3]*t_tou)   
					result.hgy_result2['s'] 	 = round(rel[4]*t_tou)   
			elif(rel[0] == 9):
				result.ph22 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['s2']['s1'] = t_tou  
					result.hgy_result1['f'] 	 = round(rel[3]*t_tou)   
					result.hgy_result2['f'] 	 = round(rel[4]*t_tou)   
			elif(rel[0] == 10):
				result.ph21 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['s2']['f1'] = t_tou  
					result.hgy_result1['f'] 	 = round(rel[3]*t_tou)   
					result.hgy_result2['s'] 	 = round(rel[4]*t_tou)   
			elif(rel[0] == 11):
				result.ph22 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['f2']['s1'] = t_tou  
					result.hgy_result1['s'] 	 = round(rel[3]*t_tou)   
					result.hgy_result2['f'] 	 = round(rel[4]*t_tou)   
			elif(rel[0] == 12):
				result.ph21 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['f2']['f1'] = t_tou  
					result.hgy_result1['s'] 	 = round(rel[3]*t_tou)   
					result.hgy_result2['s'] 	 = round(rel[4]*t_tou)   
			elif(rel[0] == 13):
				result.ph22 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['s2']['s2'] = t_tou  
					result.hgy_result1['f'] 	 = round(rel[3]*t_tou)   
					result.hgy_result2['f'] 	 = round(rel[4]*t_tou)   
			elif(rel[0] == 14):
				result.ph21 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['s2']['f2'] = t_tou  
					result.hgy_result1['f'] 	 = round(rel[3]*t_tou)   
					result.hgy_result2['s'] 	 = round(rel[4]*t_tou)   
			elif(rel[0] == 15):
				result.ph22 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['f2']['s2'] = t_tou  
					result.hgy_result1['s'] 	 = round(rel[3]*t_tou)   
					result.hgy_result2['f'] 	 = round(rel[4]*t_tou)   
			elif(rel[0] == 16):
				result.ph21 = rel[1]
				if(rel[2] <= 0):
					result.ok   = 1
					result.tc_result['f2']['f2'] = t_tou  
					result.hgy_result1['s'] 	 = round(rel[3]*t_tou)   
					result.hgy_result2['s'] 	 = round(rel[4]*t_tou)   
			else:
				pass
		else:
			pass
			
		return   result
		
	def  process03(self,alpha=0.08,t_tou = 10000):
		match1 = self.__match1_get()   
		match2 = self.__match2_get()
		result = Result_infor()  
		
		pass
		
		return   result
				
	@result_trans
	def cs_process01(self,alpha=0.08,t_tou = 10000):	
		return	self.process01(alpha,t_tou)
		
	@result_trans
	def cs_process02(self,alpha=0.08,t_tou = 10000):	
		return	self.process02(alpha,t_tou)
		
	@result_trans
	def cs_process03(self,alpha=0.08,t_tou = 10000):	
		return	self.process03(alpha,t_tou)
		
	@property
	def cs_processor( self ):
		return  self.__processor
		    
###########################
# module test_bench
###########################		
if __name__ == '__main__':    
#	#第一场盘口信息
#	tc1 = Spf_pan_infor('tc1',(2.2,2.54,2.68),0)
#	tc2 = Spf_pan_infor('tc2',(2.8,2.24,2.68),-1)
#	hgo = Spf_pan_infor('hgo',(2.2,2.12,2.68),0)    
#	hgy = Yp_pan_infor('hgy',(1.01,0.86),-0.5)  
#	
#	#第二场盘口信息
#	tc1_b = Spf_pan_infor('tc1',(1.2,2.54,4.68),0)
#	tc2_b = Spf_pan_infor('tc2',(2.1,2.24,2.08),-1)  
#	hgy_b = Yp_pan_infor('hgy',(0.95,0.89),-0.5)  

	#第一场盘口信息
	tc1 = Spf_pan_infor('tc1',(6.15,4.15,1.38),0)
	tc2 = Spf_pan_infor('tc2',(2.55,3.35,2.28),1)   
	hgy = Yp_pan_infor('hgy',(1.01,0.89),1)  
	
	#第二场盘口信息
	tc1_b = Spf_pan_infor('tc1',(2.02,3.45,2.92),0)
	tc2_b = Spf_pan_infor('tc2',(3.95,3.8,1.63),-1)  
	hgy_b = Yp_pan_infor('hgy',(0.98,0.92),-0.25) 	

	#生成两场比赛的所有信息
	m_infor1 = Match_infor('hm',tc1,tc2,hgy)  
	m_infor2 = Match_infor('rk',tc1_b,tc2_b,hgy_b)  

	for k in m_infor1:
		if(m_infor1[k]):
			print(k,m_infor1[k].plv,m_infor1[k].pankou)
	for k in m_infor2:
		if(m_infor2[k]):
			print(k,m_infor2[k].plv,m_infor2[k].pankou)
#		
#	print(len(m_infor1))
#	m_infor1['hgo'] = hgo 
#	print(m_infor1['hgo'].plv)
#	print(len(m_infor1))
		
	#把信息输入到比赛处理类，生成对象
	processor = Match_processor(m_infor1,m_infor2)
	
	#利用比赛处理类的各种处理函数返回投注方案
	#以后有新的盘口计算方法都会在Match_processor添加方法来实现         
	pop1 = processor.process01(0)       
	


	#遍历体彩投注方案
	for k1,v1 in  pop1.tc_result.items() :    
		for k2,v2 in v1.items():
			print(k1,'+',k2,v2)   
	
	print(pop1.hgy_result1)        
	print(pop1.hgy_result2)
	print('ph21 = ',pop1.ph21)
	print('ph22 = ',pop1.ph22)
	
	pop2 = processor.process02()
	for k1,v1 in  pop2.tc_result.items() :    
		for k2,v2 in v1.items():
			print(k1,'+',k2,v2)   
	
	print(pop2.hgy_result1)        
	print(pop2.hgy_result2)
	print('ph21 = ',pop2.ph21)
	print('ph22 = ',pop2.ph22)




		

		



	

	
	


	
	
	
	


