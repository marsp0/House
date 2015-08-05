import Tkinter as tk
from house import Properties,House,Apartment
import excep as ex
import tkMessageBox as mb
import tkFileDialog as fd


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
						'owner_phone':tk.StringVar(),
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
						'rooms':tk.IntVar(),
						'floors':tk.IntVar(),
						'floor':tk.IntVar(),
						'max_floors':tk.IntVar(),
						'house':tk.BooleanVar(),
						'description':tk.StringVar()}

		self.first_column_frame = tk.Frame(self.add_property_display,bd=2,relief='raised')
		self.house_frame = tk.Frame(self.first_column_frame,bd=2,relief='raised')
		self.for_sale_frame = tk.Frame(self.first_column_frame,bd=2,relief='raised')
		self.parno_frame = tk.Frame(self.first_column_frame,bd=2,relief='raised')
		self.owner_frame = tk.Frame(self.first_column_frame,bd=2,relief='raised')

		self.second_column_frame = tk.Frame(self.add_property_display,bd=2,relief='raised')
		self.garage_frame = tk.Frame(self.second_column_frame,bd=2,relief='raised')
		self.attic_frame = tk.Frame(self.second_column_frame,bd=2,relief='raised')
		self.owner_phone_frame = tk.Frame(self.second_column_frame,bd=2,relief='raised')
		self.furniture_frame = tk.Frame(self.second_column_frame,bd=2,relief='raised')

		self.third_column_frame = tk.Frame(self.add_property_display,bd=2,relief='raised')
		self.basement_frame = tk.Frame(self.third_column_frame,bd=2,relief='raised')
		self.yard_frame = tk.Frame(self.third_column_frame,bd=2,relief='raised')
		self.tec_frame = tk.Frame(self.third_column_frame,bd=2,relief='raised')
		self.price_frame = tk.Frame(self.third_column_frame,bd=2,relief='raised')

		self.address_frame = tk.Frame(self.add_property_display,bd=3,relief='raised')
		self.square_meters_frame = tk.Frame(self.add_property_display,bd=3,relief='raised')

		self.additional_info_frame = tk.Frame(self.add_property_display,bd=2,relief='raised')
		self.floors_frame = tk.Frame(self.additional_info_frame,bd=2,relief='raised')
		self.rooms_frame = tk.Frame(self.additional_info_frame,bd=2,relief='raised')
		self.max_floors_frame = tk.Frame(self.additional_info_frame,bd=2,relief='raised')
		self.floor_frame = tk.Frame(self.additional_info_frame,bd=2,relief='raised')


		self.main_view()

	def packer(self,to_unpack,to_pack,*args):
		for child in to_unpack.winfo_children():
			child.destroy()
		to_unpack.pack_forget()
		to_pack(*args)

	def grider(self,to_ungrid,to_grid,*args):
		for child in to_ungrid.winfo_children():
			if isinstance(child,tk.Frame):
				child.grid_forget()
			else:
				child.destroy()
		to_ungrid.grid_forget()
		to_grid(*args)


	def main_view(self):
		self.main_display.pack()
		tk.Button(self.main_display,text='Add Property',command=lambda : self.packer(self.main_display,self.add_property_view)).grid(row=0,column=0)
		tk.Button(self.main_display,text='Quit',command=self.quit).grid(row=0,column=1)

	def add_property_view(self):

		self.add_property_display.pack()

		self.first_column_frame.grid(row=1,column=1)
		self.house_frame.grid(row=1,column=1)
		self.for_sale_frame.grid(row=2,column=1)
		self.parno_frame.grid(row=3,column=1)
		self.owner_frame.grid(row=4,column=1)

		self.second_column_frame.grid(row=1,column=2)
		self.garage_frame.grid(row=1,column=1)
		self.attic_frame.grid(row=2,column=1)
		self.furniture_frame.grid(row=3,column=1)
		self.owner_phone_frame.grid(row=4,column=1)

		self.third_column_frame.grid(row=1,column=3)
		self.basement_frame.grid(row=1,column=1)
		self.yard_frame.grid(row=2,column=1)
		self.tec_frame.grid(row=3,column=1)
		self.price_frame.grid(row=4,column=1)

		self.address_frame.grid(row=2,column=1,columnspan=2)
		self.square_meters_frame.grid(row=2,column=3)
		
		#17 / 41
		tk.Label(self.add_property_display,text='Add Property',width=84,bd=5,relief='raised').grid(row=0,column=1,columnspan=6)
		

		tk.Label(self.house_frame,text = 'Type',width=9).grid(row=1,column=1)
		tk.Radiobutton(self.house_frame,text='House',width=8,variable = self.add_vars['house'],value=True,command=lambda : self.grider(self.additional_info_frame,self.add_aditional_info,'house')).grid(row=1,column=2)
		tk.Radiobutton(self.house_frame,text='Flat',width=8,variable = self.add_vars['house'],value=False,command=lambda : self.grider(self.additional_info_frame,self.add_aditional_info,'apartment')).grid(row=1,column=3)

		tk.Label(self.for_sale_frame,text='For sale',width=21).grid(row=1,column=1)
		tk.Checkbutton(self.for_sale_frame,text=' ',variable=self.add_vars['for_sale'],width=5).grid(row=1,column=2)

		tk.Label(self.garage_frame,text='Garage',width=21).grid(row=1,column=1)
		tk.Checkbutton(self.garage_frame,text='',variable=self.add_vars['garage'],width=5).grid(row=1,column=2)

		tk.Label(self.basement_frame,text='Basement',width=21).grid(row=1,column=1)
		tk.Checkbutton(self.basement_frame,text='',variable=self.add_vars['basement'],width=4).grid(row=1,column=2)
 
		tk.Label(self.attic_frame,text='Attic',width=21).grid(row=1,column=1)
		tk.Checkbutton(self.attic_frame,text='',variable=self.add_vars['attic'],width=5).grid(row=1,column=2)

		tk.Label(self.yard_frame,text='Yard',width=21).grid(row=1,column=1)
		tk.Checkbutton(self.yard_frame,text='',variable=self.add_vars['yard'],width=4).grid(row=1,column=2)

		tk.Label(self.parno_frame,text='Parno',width=21).grid(row=1,column=1)
		tk.Checkbutton(self.parno_frame,text=' ',variable=self.add_vars['parno'],width=5).grid(row=1,column=2)

		tk.Label(self.furniture_frame,text='Furniture',width=21).grid(row=1,column=1)
		tk.Checkbutton(self.furniture_frame,text='',variable=self.add_vars['furniture'],width=5).grid(row=1,column=2)

		tk.Label(self.tec_frame,text='TEC',width=21).grid(row=1,column=1)
		tk.Checkbutton(self.tec_frame,text='',variable=self.add_vars['tec'],width=4).grid(row=1,column=2)

		tk.Label(self.owner_frame,text='Owner',width=6).grid(row=1,column=1)
		tk.Entry(self.owner_frame,textvariable=self.add_vars['owner'],width=19).grid(row=1,column=2)

		tk.Label(self.owner_phone_frame,text='Phone',width=6).grid(row=1,column=1)
		tk.Entry(self.owner_phone_frame,textvariable=self.add_vars['owner_phone'],width=19).grid(row=1,column=2)

		tk.Label(self.price_frame,text='Price',width=6).grid(row=1,column=1)
		tk.Entry(self.price_frame,textvariable=self.add_vars['price'],width=18).grid(row=1,column=2)

		tk.Label(self.address_frame,text='Address',width=7).grid(row=1,column=1)
		tk.Entry(self.address_frame,textvariable=self.add_vars['address'],width=47).grid(row=1,column=2)

		tk.Label(self.square_meters_frame,text='Square Meters').grid(row=1,column=1)
		tk.Entry(self.square_meters_frame,textvariable=self.add_vars['square_meters'],width=12).grid(row=1,column=2)


		

	def add_aditional_info(self,option):
		self.additional_info_frame.grid(row=3,column=1,columnspan=3)
		if option == 'house':
			self.floors_frame.grid(row=1,column=3)
			tk.Label(self.floors_frame,text='Floors',width=10).grid(row=1,column=1)
			tk.Entry(self.floors_frame,textvariable=self.add_vars['floors'],width=14).grid(row=1,column=2)

			tk.Label(self.additional_info_frame,text='Description',width=57,bd=2,relief='raised',pady=6).grid(row=1,column=1,columnspan=2)
			tk.Entry(self.additional_info_frame,textvariable=self.add_vars['description'],width=83).grid(row=2,column=1,columnspan=3)
		elif option == 'apartment':
			self.rooms_frame.grid(row=1,column=1)
			self.max_floors_frame.grid(row=1,column=2)
			self.floor_frame.grid(row=1,column=3)
			tk.Label(self.rooms_frame,text='Rooms',width=10).grid(row=1,column=1)
			tk.Entry(self.rooms_frame,textvariable=self.add_vars['rooms'],width=15).grid(row=1,column=2)

			tk.Label(self.max_floors_frame,text='Max Floors',width=10).grid(row=1,column=1)
			tk.Entry(self.max_floors_frame,textvariable=self.add_vars['max_floors'],width=16).grid(row=1,column=2)

			tk.Label(self.floor_frame,text='Floor',width=9).grid(row=1,column=1)
			tk.Entry(self.floor_frame,textvariable=self.add_vars['floor'],width=15).grid(row=1,column=2)

			tk.Label(self.additional_info_frame,text='Description',pady=6,bd=2,relief='raised',width=84).grid(row=2,column=1,columnspan=3)
			tk.Entry(self.additional_info_frame,textvariable=self.add_vars['description'],width=83).grid(row=3,column=1,columnspan=3)


	def quit(self):
		self.properties.stop_database()
		self.master.quit()

if __name__=='__main__':
	gui = Gui()
	gui.mainloop()