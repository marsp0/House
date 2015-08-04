import Tkinter as tk
from house import Properties,House,Apartment


class Gui(tk.Frame):

	def __init__(self,parent=None,*args,**kwargs):

		tk.Frame.__init__(self,parent,*args,**kwargs)

		self.master.maxsize(width=600,height=400)
		self.master.minsize(width=600,height=400)
		self.master.title('MyHouse')
		self.pack()

		self.properties = Properties()

		''' MAIN VIEW'''
		self.main_display = tk.Frame(self)

		'''ADD VIEW'''
		self.add_property_display = tk.Frame(self)
		self.add_vars = {'for_sale':tk.BooleanVar(),
						'owner' : tk.StringVar(),
						'owner_phone':tk.IntVar(),
						'price':tk.IntVar(),
						'address':tk.StringVar(),
						'square_meters':tk.IntVar(),
						'garage':tk.BooleanVar(),
						'attic':tk.BooleanVar(),
						'basement':tk.BooleanVar(),
						'yard':tk.BooleanVar(),
						'furniture':tk.BooleanVar(),
						'parno':tk.BooleanVar(),
						'tec':tk.BooleanVar(),
						'description':tk.StringVar(),
						'rooms':tk.IntVar(),
						'floors':tk.IntVar(),
						'floor':tk.IntVar(),
						'max_floors':tk.IntVar()}

		self.main_view()

	def packer(self,to_unpack,to_pack,*args):
		for child in to_unpack.winfo_children():
			child.destroy()
		to_unpack.pack_forget()
		to_pack(*args)


	def main_view(self):
		self.main_display.pack()

		tk.Button(self.main_display,text='Add Property',command=lambda : self.packer(self.main_display,self.add_property_view)).grid(row=0,column=0)
		tk.Button(self.main_display,text='Edit Property').grid(row=0,column=1)
		tk.Button(self.main_display,text='Delete Property').grid(row=0,column=2)
		tk.Button(self.main_display,text='Quit',command=self.quit).grid(row=0,column=3)

	def add_property_view(self):
		self.add_property_display.pack()
		tk.Button(self.add_property_display,text='Add House',command = lambda : self.packer(self.add_property_display,self.add_property_form,'house')).grid(row=0,column=0)
		tk.Button(self.add_property_display,text='Add Apartment',command = lambda : self.packer(self.add_property_display,self.add_property_form,'apartment')).grid(row=0,column=1)
		tk.Button(self.add_property_display,text='Back',command = lambda : self.packer(self.add_property_display,self.main_view)).grid(row=0,column=2)

	def add_property_form(self,option):
		self.add_property_display.pack()
		tk.Label(self.add_property_display,text='Add {} Form'.format(option.capitalize())).grid(row=0,column=0,columnspan=6)
		tk.Label(self.add_property_display,text='For Sale').grid(row=1,column=1)
		tk.Radiobutton(self.add_property_display,text='Yes',value=True,variable=self.add_vars['for_sale']).grid(row=1,column=2)
		tk.Radiobutton(self.add_property_display,text='No',value=False,variable=self.add_vars['for_sale']).grid(row=1,column=3)

		tk.Label(self.add_property_display,text='Owner').grid(row=1,column=4)
		tk.Entry(self.add_property_display,textvariable=self.add_vars['owner']).grid(row=1,column=5,columnspan=2)
		
		tk.Label(self.add_property_display,text='Owner\'s Phone').grid(row=2,column=1)
		tk.Entry(self.add_property_display,textvariable=self.add_vars['owner_phone']).grid(row=2,column=2,columnspan=2)
		
		tk.Label(self.add_property_display,text='Price').grid(row=2,column=4)
		tk.Entry(self.add_property_display,textvariable=self.add_vars['price']).grid(row=2,column=5,columnspan=2)
		
		tk.Label(self.add_property_display,text = 'Address').grid(row=3,column=1)
		tk.Entry(self.add_property_display,textvariable=self.add_vars['address']).grid(row=3,column=2,columnspan=2)
		
		tk.Label(self.add_property_display,text = 'Square Meters').grid(row=3,column=4)
		tk.Entry(self.add_property_display,textvariable=self.add_vars['square_meters']).grid(row=3,column=5,columnspan=2)
		
		#tk.Label(self.add_property_display,text = 'Description').grid(row=4,column=1)
		#tk.Entry(self.add_property_display,textvariable=self.add_vars['description']).grid(row=4,column=2,columnspan=2)
		
		tk.Label(self.add_property_display,text='Garage').grid(row=4,column=1)
		tk.Radiobutton(self.add_property_display,text='Yes',value=True,variable=self.add_vars['garage']).grid(row=4,column=2)
		tk.Radiobutton(self.add_property_display,text='No',value=False,variable=self.add_vars['garage']).grid(row=4,column=3)
		
		tk.Label(self.add_property_display,text='Basement').grid(row=4,column=4)
		tk.Radiobutton(self.add_property_display,text='Yes',value=True,variable=self.add_vars['basement']).grid(row=4,column=5)
		tk.Radiobutton(self.add_property_display,text='No',value=False,variable=self.add_vars['basement']).grid(row=4,column=6)
		
		tk.Label(self.add_property_display,text='Attic').grid(row=5,column=1)
		tk.Radiobutton(self.add_property_display,text='Yes',value=True,variable=self.add_vars['attic']).grid(row=5,column=2)
		tk.Radiobutton(self.add_property_display,text='No',value=False,variable=self.add_vars['attic']).grid(row=5,column=3)
		
		tk.Label(self.add_property_display,text='Yard').grid(row=5,column=4)
		tk.Radiobutton(self.add_property_display,text='Yes',value=True,variable=self.add_vars['yard']).grid(row=5,column=5)
		tk.Radiobutton(self.add_property_display,text='No',value=False,variable=self.add_vars['yard']).grid(row=5,column=6)
		
		tk.Label(self.add_property_display,text='Furniture').grid(row=6,column=1)
		tk.Radiobutton(self.add_property_display,text='Yes',value=True,variable=self.add_vars['furniture']).grid(row=6,column=2)
		tk.Radiobutton(self.add_property_display,text='No',value=False,variable=self.add_vars['furniture']).grid(row=6,column=3)
		
		tk.Label(self.add_property_display,text='Parno').grid(row=6,column=4)
		tk.Radiobutton(self.add_property_display,text='Yes',value=True,variable=self.add_vars['parno']).grid(row=6,column=5)
		tk.Radiobutton(self.add_property_display,text='No',value=False,variable=self.add_vars['parno']).grid(row=6,column=6)
		
		tk.Label(self.add_property_display,text='TEC').grid(row=7,column=1)
		tk.Radiobutton(self.add_property_display,text='Yes',value=True,variable=self.add_vars['tec']).grid(row=7,column=2)
		tk.Radiobutton(self.add_property_display,text='No',value=False,variable=self.add_vars['tec']).grid(row=7,column=3)
		row=7
		if option=='house':
			tk.Label(self.add_property_display,text='Floors').grid(row=row,column=4)
			tk.Entry(self.add_property_display,textvariable=self.add_vars['floors']).grid(row=row,column=5,columnspan=2)
			row += 1
		elif option =='apartment':
			tk.Label(self.add_property_display,text='Floor').grid(row=row,column=4)
			tk.Entry(self.add_property_display,textvariable=self.add_vars['floor']).grid(row=row,column=5,columnspan=2)
			row += 1
			tk.Label(self.add_property_display,text='Max Floors').grid(row=row,column=1)
			tk.Entry(self.add_property_display,textvariable=self.add_vars['max_floors']).grid(row=row,column=2,columnspan=2)

			tk.Label(self.add_property_display,text='Rooms').grid(row=row,column=4)
			tk.Entry(self.add_property_display,textvariable=self.add_vars['rooms']).grid(row=row,column=5,columnspan=2)
			row += 1

		tk.Label(self.add_property_display,text='Description').grid(row=row,column=1)
		row += 1
		tk.Text(self.add_property_display,textvariable=self.add_vars['description']).grid(row=row,column=1,columnspan=6)
		row += 1
		tk.Button(self.add_property_display,text='Back',command = lambda : self.packer(self.add_property_display,self.main_view)).grid(row=row,column=5)
		tk.Button(self.add_property_display,text='Save').grid(row=row,column=6)

	def quit(self):
		self.properties.stop_database()
		self.master.quit()

if __name__=='__main__':
	gui = Gui()
	gui.mainloop()