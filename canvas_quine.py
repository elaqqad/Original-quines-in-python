l=[
   'x=[319,109,249,193,159,67,79,300,79,198,79,216,78,95,299,89,229,173,139,47,59,280,57,178,59,196,58,75]',
   'from Tkinter import*',
   'fen=Tk();can=Canvas(fen,bg="white",width=900, height=900);can.pack()',
   'can.create_rectangle(0,0,40,900, fill="gray",width=0)',
   'can.create_text(42,20,text="   1      l=[")',
   'k=1',
   'for i in l :',
   '    can.create_text(x[k-1],20*(k+1),text="   "+str(k+1)+"      "+"           "+chr(39)+i+chr(39)+",")',
   '    k=k+1',  
   'can.create_text(38,20*(k+1),text="   "+str(k+1)+"      ]")',
   'for i in l :',
   '    can.create_text(x[k-1],20*(k+2),text="   "+str(k+2)+"      "+i )', 
   '    k=k+1',
   'fen.mainloop()',    
]
x=[319,109,249,193,159,67,79,300,79,198,79,216,78,95,299,89,229,173,139,47,59,280,57,178,59,196,58,75]
from Tkinter import*
fen=Tk();can=Canvas(fen,bg="white",width=900, height=900);can.pack()
can.create_rectangle(0,0,40,900, fill="gray",width=0)
can.create_text(42,20,text="   1      l=[")
k=1
for i in l :
    can.create_text(x[k-1],20*(k+1),text="   "+str(k+1)+"      "+"           "+chr(39)+i+chr(39)+",")
    k=k+1   
can.create_text(38,20*(k+1),text="   "+str(k+1)+"      ]")
for i in l :
    can.create_text(x[k-1],20*(k+2),text="   "+str(k+2)+"      "+i )
    k=k+1      
fen.mainloop()