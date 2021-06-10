class Monado(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def bind(self,fn):
        return self >> fn    



class Nothing:
    def __init__(self):
        self.name = self

    def __repr__(self):
        return 'Nothing'

    def __str__(self):
        return 'Nothing'    

    def __rshift__(self,fn):
        return self  

    def __eq__(self,other):
        return type(self.name) == type(other)

class MaybeInt(Monado):
    def __eq__(self,other):
        return self.name == other   
        
    def __rshift__(self,fn):
        try:
            self = int(str(self))
            return MaybeInt(fn(self))
        except Exception:
            return Nothing()

    def __repr__(self):
        return f'MaybeInt: {self.name}'
             

class MaybeFloat(Monado):    
    def __rshift__(self,fn):
        try:
            self = float(str(self))
            return MaybeFloat(fn(self))
        except Exception:
            return Nothing()

    def __eq__(self,other):
        return self.name == other  
    
    def __repr__(self):
        return f'MaybeFloat: {self.name}'


class MaybeStr(Monado):
    def __rshift__(self, fn):
         try:
            self = str(self)
            return MaybeStr(fn(self))
         except Exception:
            return Nothing()

    def __eq__(self,other):
        return self.name == other   

    def __repr__(self):
        return f'MaybeStr: {self.name}'         

class Left(Monado):
    def __repr__(self):
        return f'Left {self.name}'    

    def __rshift__(self,fn):
        return self 

    def __eq__(self,other):
        return self.name == other 


class EitherInt(Monado):
    def __rshift__(self,fn):
        try:
            self = int(str(self))
            return EitherInt(fn(self))
        except Exception:
            return Left(self)

    def __eq__(self,other):
        return self.name == other  

    def __repr__(self):
        return f'EitherInt: {self.name}'
   

class EitherFloat(Monado):
    def __rshift__(self,fn):
        try:
            self = float(str(self))
            return EitherFloat(fn(self))
        except Exception:
            return Left(self)

    def __eq__(self,other):
        return self.name == other     

    def __repr__(self):
        return f'EitherFloat: {self.name}'
          

class EitherStr(Monado):
    def __rshift__(self,fn):
        try:
            self = str(self)
            return EitherStr(fn(self))
        except Exception:
            return Left(self)

    def __eq__(self,other):
       return self.name == other  

    def __repr__(self):
        return f'EitherStr: {self.name}'
   

class Failure(Monado):
    def __init__(self,er,name):
        self.name = name
        self.er = er

    def __repr__(self):
        return f'Failure {self.name}'  

    def __str__(self):
        return f'Failure {self.name}' 

    def __rshift__(self,fn):
        return self    

    def __eq__(self,other):
        return self.name == other 



class ErrorInt(Monado):
    def __rshift__(self,fn):
        try:
            self = int(str(self))
            return ErrorInt(fn(self))
        except Exception as er:
            return (Failure(er,self))

    def __eq__(self,other):
        return self.name == other     


class ErrorFloat(Monado):
    def __rshift__(self,fn):
        try:
            self = float(str(self))
            return ErrorFloat(fn(self))
        except Exception as er:
            return (Failure(er,self))    

    def __eq__(self,other):
        return self.name == other  


class ErrorStr(Monado):
    def __rshift__(self,fn):
        try:
            self = str(self)
            return ErrorStr(fn(self))
        except Exception as er:
            return (Failure(er,self))                

    def __eq__(self,other):
        return self.name == other  

class IO_false(Monado):
    def __rshift__(self,fn):
        return self

    def __eq__(self,other):
        return self.name == other

    #def __str__(self):
        #return f'IO false: {self.name}'    

    #def __repr__(self):
        #return f'IO false: {self.name}'     

class IO(Monado):
    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'    

    def __rshift__(self, fn):
        try:
            self = str(self)
            return IO(fn(self))
        except Exception as er:
            return IO_false(f'IO Monad error: {er}')

    def __eq__(self,other):
        return self.name == other   

        
class MonadoList(Monado):

    def __rshift__(self,fn):
        if isinstance(self.name,list):
            try:
                return MonadoList(list(map(fn,self.name)))
            except Exception:
                return MonadoList([])
        else:
            return []        

    def __eq__(self,other):
        return self.name == other  
            
def convectM(obj,pClass):
    p = (MaybeFloat,MaybeInt,MaybeStr,EitherStr,EitherFloat,EitherInt,ErrorStr,ErrorFloat,ErrorInt,IO)
    if issubclass(pClass, p):
        return pClass(obj)
    else:
        if issubclass(pClass, MonadoList) and type(obj) == type(list()):
            return pClass(obj)        
        else:
            raise TypeError('ConvectError: pClass != MonadClass')

    
