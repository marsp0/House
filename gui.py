import Tkinter as tk
from house import Properties,Apartment,House
import excep as ex


class Gui(tk.Frame):

	def __init__(self,parent=None,*args,**kwargs):
		tk.Frame.__init__(self,parent,*args,**kwargs)
		self.master.minsize(width=600,height=400)
		self.master.maxsize(width=600,height=400)
		self.pack()

		self.main_display = tk.Frame(self)
		

		self.add_view = AddView(self)
		self.properties = Properties()
		self.main_view()

	def main_view(self):
		self.main_display_buttons = tk.Frame(self.main_display)
		self.main_display_properties = tk.Frame(self.main_display)
		self.main_display.pack()
		self.main_display_buttons.pack(anchor='w')
		self.main_display_properties.pack(anchor='e')

		tk.Button(self.main_display_buttons,text='Add Property',command = lambda : self.packer(self.main_display,self.add_view.ask_view)).grid(row=1,column=1)
		tk.Button(self.main_display_buttons,text='View Houses').grid(row=2,column=1)
		tk.Button(self.main_display_buttons,text='View Flats').grid(row=3,column=1)
		tk.Button(self.main_display_buttons,text='Quit').grid(row=4,column=1)

	def packer(self,to_unpack,to_pack):
		for child in to_unpack.winfo_children():
			child.destroy()
		to_unpack.pack_forget()
		to_pack()

	def back(self,to_hide,to_show):
		to_hide()
		to_show()

	def quit(self):
		self.properties.stop_database()
		self.master.quit()


class AddView(tk.Frame):

	def __init__(self,parent=None,*args,**kwargs):
		tk.Frame.__init__(self,parent,*args,**kwargs)

		self.vars = {'owner':tk.StringVar(),
					'house':tk.BooleanVar(),
					'for_sale':tk.BooleanVar(),
					'owner_phone': tk.StringVar(),
					'address':tk.StringVar(),
					'basement':tk.BooleanVar(),
					'attic':tk.BooleanVar(),
					'yard':tk.BooleanVar(),
					'garage':tk.BooleanVar(),
					'price':tk.IntVar(),
					'square_meters':tk.IntVar(),
					'furniture':tk.BooleanVar(),
					'parno':tk.BooleanVar(),
					'tec':tk.BooleanVar(),
					'rooms':tk.IntVar(),
					'floors':tk.IntVar(),
					'floor':tk.IntVar(),
					'max_floors':tk.IntVar(),
					'description':tk.StringVar()}

		self.additional_frame = tk.Frame(self)

		self.main_options = (('House','For sale'),('Owner','Owner phone'),('Address','Square meters'),('Price','Garage'),('Description',None),
							('Yard','Attic'),('Basement','Furniture'),('Parno','TEC'))
		self.flat_options = ('Rooms','Max floors','Floor')

		self.save_house_values = ('owner','house','for_sale','owner_phone','address','basement',
									'attic','yard','garage','price','square_meters','furniture',
									'parno','tec','floors','description')
		self.save_flat_values = ('owner','house','for_sale','owner_phone','address','basement',
									'attic','yard','garage','price','square_meters','furniture',
									'parno','tec','description','rooms','floor','max_floors')

	def ask_view(self):
		self.pack()
		row = 1
		tk.Label(self,text='Add Property',bd=3,relief='raised',width=84,pady=6).grid(row=0,column=1,columnspan=4)
		for var1, var2 in self.main_options:
			if None not in (var1,var2):
				var1_var = var1.lower().replace(' ','_')
				var2_var = var2.lower().replace(' ','_')
				tk.Label(self,text=var1,relief='raised',bd=2,width=20,pady=3).grid(row=row,column=1)
				tk.Label(self,text=var2,relief='raised',bd=2,width=20,pady=3).grid(row=row,column=3)
				if isinstance(self.vars[var1_var],tk.BooleanVar):
					if var1 == 'House':
						tk.Checkbutton(self,variable = self.vars[var1_var],command=self.add_additional_frame,bd=2,relief='raised').grid(row=row,column=2)
					else:
						tk.Checkbutton(self,variable = self.vars[var1_var],bd=2,relief='raised').grid(row=row,column=2)
				elif isinstance(self.vars[var1_var],tk.IntVar) or isinstance(self.vars[var1_var],tk.StringVar):
					tk.Entry(self,textvariable=self.vars[var1_var]).grid(row=row,column=2)
				if isinstance(self.vars[var2_var],tk.BooleanVar):
					tk.Checkbutton(self,variable=self.vars[var2_var]).grid(row=row,column=4)
				elif isinstance(self.vars[var2_var],tk.IntVar) or isinstance(self.vars[var2_var],tk.StringVar):
					tk.Entry(self,textvariable=self.vars[var2_var]).grid(row=row,column=4)
			else:
				tk.Label(self,text=var1,width=20,relief='raised',bd=2,pady=3).grid(row=row,column=1)
				tk.Entry(self,textvariable=self.vars['description'],width=63).grid(row=row,column=2,columnspan=3)
			row+=1

	def add_additional_frame(self):
		self.additional_frame.grid(row=9,column=1,columnspan=4)
		for child in self.additional_frame.winfo_children():
			child.destroy()
		row = 1
		width=17
		if self.vars['house'].get() == 0:
			tk.Label(self.additional_frame,text='Floors',width=20,relief='raised',bd=2,pady=3).grid(row=row,column=1)
			tk.Entry(self.additional_frame,textvariable=self.vars['floors']).grid(row=row,column=2)
			width=19
		else:
			column=1
			for var in self.flat_options:
				if self.flat_options.index(var) % 2 == 0:
					row += 1
					column = 1
				tk.Label(self.additional_frame,text=var,width=20,bd=2,relief='raised',pady=3).grid(row=row,column=column)
				tk.Entry(self.additional_frame,textvariable=self.vars[var.lower().replace(' ','_')]).grid(row=row,column=column + 1)
				column += 2
		tk.Button(self.additional_frame,text='Back',width=16,command = lambda : self.master.back(self.hide,self.master.main_view)).grid(row=row,column=3)
		tk.Button(self.additional_frame,text='Save',width=width,command = self.save_property).grid(row=row,column=4)

	def save_property(self):
		to_return = {}
		try:
			self.check_fields()
			if self.vars['house'].get() == 0:
				for value in self.save_house_values:
					to_return[value] = self.vars[value].get()
				print to_return
			else:
				for value in self.save_flat_values:
					to_return[value] = self.vars[value].get()
				print  to_return
		except ex.InvalidValue:
			mb.showwarning('Invalid Values','Some of the values that you\'ve entered are not valid')

	def check_fields(self):
		if self.vars['address'].get() == '' or self.vars['owner'].get() == '' or self.vars['owner_phone'].get() == '' or \
		self.vars['price'].get() == 0 or self.vars['square_meters'].get() == 0:
			raise ex.InvalidValue(0)
		if self.vars['house'].get() == 0:
			if self.vars['rooms'].get() == 0 or self.vars['max_floors'].get() == 0:
				raise ex.InvalidValue(0)
		else:
			if self.vars['floors'].get() == 0:
				raise ex.InvalidValue(0)

	def show_view(self,info_dict):
		self.pack()
		row=1
		tk.Label(self,text='View Property',width=84,pady=6,bd=2,relief='raised').grid(row=0,column=1,columnspan=4)
		for var1,var2 in self.main_options:
			if None not in (var1,var2):
				info_key1 = var1.lower().replace(' ','_')
				info_key2 = var2.lower().replace(' ','_')
				tk.Label(self,text=var1,width=20,bd=2,relief='raised',pady=3).grid(row=row,column=1)
				tk.Label(self,text=self.get_value(info_dict[info_key1]),width=21,bd=2,relief='raised',pady=3).grid(row=row,column=2)

				tk.Label(self,text=var2,width=20,bd=2,relief='raised',pady=3).grid(row=row,column=3)
				tk.Label(self,text=self.get_value(info_dict[info_key2]),width=21,bd=2,relief='raised',pady=3).grid(row=row,column=4)
			else:

				tk.Label(self,text='Description',width=20,bd=2,relief='raised',pady=3).grid(row=row,column=1)
				tk.Label(self,text=info_dict['description'],width=64,bd=2,relief='raised',pady=3).grid(row=row,column=2,columnspan=3)
			row += 1
		if info_dict['house']:
			tk.Label(self,text='Floors',width=20,bd=2,relief='raised',pady=3).grid(row=row,column=1)
			tk.Label(self,text=self.get_value(info_dict['floors']),width=21,bd=2,relief='raised',pady=3).grid(row=row,column=2)
		else:
			column=1
			for var in self.flat_options:
				if self.flat_options.index(var) % 2 == 0:
					row += 1
					column = 1
				tk.Label(self.additional_frame,text=var,width=20,bd=2,relief='raised',pady=3).grid(row=row,column=column)
				tk.Label(self.additional_frame,textvariable=self.get_value(var.lower().replace(' ','_'))).grid(row=row,column=column + 1)
				column += 2
		tk.Button(self,text='Back',width=16).grid(row=row,column=3)
		tk.Button(self,text='Sell/Rent',width=16).grid(row=row,column=4)


	def get_value(self,some_str):
		if some_str == 1:
			return 'Yes'
		elif some_str == 0:
			return 'No'
		else:
			return some_str


	def hide(self):
		self.pack_forget()
		for child in self.winfo_children():
			if isinstance(child, tk.Frame):
				try:
					child.pack_forget()
				except:
					child.grid_forget()
			else:
				child.destroy()

if __name__=='__main__':
	p = Gui()
	p.mainloop()