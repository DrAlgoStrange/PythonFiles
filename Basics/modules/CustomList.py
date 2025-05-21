import ctypes


class Modifyed_list():
    def __init__(self):
        self.capacity=1
        self.size=0
        self.array=self.__makearray(self.capacity)

    def __makearray(self, capacity):
        return (capacity*ctypes.py_object)()
    
    def __resize(self,capacity):
        new_array= self.__makearray(capacity)
        for i in range(self.size):
            new_array[i]=self.array[i]
        self.array=new_array
    
    def append(self,item,index=-1):
        if self.size==self.capacity:
            self.capacity=self.capacity*2
            self.__resize(self.capacity)
        if index==-1:
            self.array[self.size]=item
            self.size+=1
        else:
            for i in range(self.size,index,-1):
                self.array[i]=self.array[i-1]
            self.array[index]=item
            self.size+=1

    def __str__(self):
        array_output=""
        for i in range(self.size):
            array_output+=str(self.array[i])+" "
        return f"[{array_output.strip(" ")}]"
    
    def __getitem__(self,index):
        return self.array[index]


