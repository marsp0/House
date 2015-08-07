import excep as ex
import shelve

class Property(object):

	def __new__(cls,*args,**kwargs):
		obj = object.__new__(cls,*args,**kwargs)

		if not hasattr(cls,'rent_house_ids'):
			cls.rent_house_ids = 1000000
		if not hasattr(cls,'sale_house_ids'):
			cls.sale_house_ids = 2000000
		if not hasattr(cls,'rent_apartment_ids'):
			cls.rent_apartment_ids = 3000000
		if not hasattr(cls,'sale_apartment_ids'):
			cls.sale_apartment_ids = 4000000

		if args[0]['house'] and args[0]['for_sale']:
			obj.idd = cls.sale_house_ids
			cls.sale_house_ids += 1
		elif args[0]['house'] and not(args[0]['for_sale']):
			obj.idd = cls.rent_house_ids
			cls.rent_house_ids += 1
		elif not(args[0]['house']) and args[0]['for_sale']:
			obj.idd = cls.sale_apartment_ids
			cls.sale_apartment_ids += 1
		elif not (args[0]['for_sale'] and args[0]['house']):
			obj.idd = cls.rent_apartment_ids
			cls.rent_apartment_ids += 1

		return obj

	def __init__(self,info_dict):

		self._owner = info_dict['owner']
		self._owner_phone = info_dict['owner_phone']
		self._price = info_dict['price']
		self._address = info_dict['address']
		self._square_meters = info_dict['square_meters']
		self._garage = info_dict['garage']
		self._basement = info_dict['basement']
		self._attic = info_dict['attic']
		self._yard = info_dict['yard']
		self._furniture = info_dict['furniture']
		self._parno = info_dict['parno']
		self._tec = info_dict['tec']
		self._description = info_dict['description']

	def get_info(self):
		return {'idd' : self.idd,
				'owner':self.owner,
				'owner_phone':self.owner_phone,
				'price':self.price,
				'address':self.address,
				'square_meters':self.square_meters,
				'garage':self.garage,
				'basement':self.basement,
				'attic':self.attic,
				'yard':self.yard,
				'furniture':self.furniture,
				'parno':self.parno,
				'tec':self.tec,
				'description':self.description}

	@property
	def price(self):
		return self._price

	@price.setter
	def price(self,value):
		if isinstance(value,int):
			self._price = value
		else:
			raise ex.InvalidValue(value)

	@property
	def owner_phone(self):
		return self._owner_phone

	@owner_phone.setter
	def owner_phone(self,value):
		if isinstance(value,int) and len(str(value)) == 10:
			self._owner_phone = value
		else:
			raise ex.InvalidValue(value)

	@property
	def owner(self):
		return self._owner

	@owner.setter
	def owner(self,value):
		self._owner = value

	@property
	def address(self):
		return self._address

	@address.setter
	def address(self,value):
		self._address = value

	@property
	def square_meters(self):
		return self._square_meters

	@square_meters.setter
	def square_meters(self,value):
		if isinstance(value,int):
			self._square_meters = value
		else:
			raise ex.InvalidValue(value)

	@property
	def garage(self):
		return self._garage

	@garage.setter
	def garage(self,value):
		if value in (True,False):
			self._garage = value
		else:
			raise ex.InvalidValue(value)

	@property
	def basement(self):
		return self._basement

	@basement.setter
	def basement(self,value):
		if value in (True,False):
			self._basement = value
		else:
			raise ex.InvalidValue(value)

	@property
	def attic(self):
		return self._attic

	@attic.setter
	def attic(self,value):
		if value in (True,False):
			self._attic = value
		else:
			raise ex.InvalidValue(value)

	@property
	def yard(self):
		return self.yard

	@yard.setter
	def yard(self,value):
		if value in (True,False):
			self._yard = value
		else:
			raise ex.InvalidValue(value)

	@property
	def furniture(self):
		return self._furniture

	@furniture.setter
	def furniture(self,value):
		if value in (True,False):
			self._furniture = value
		else:
			raise ex.InvalidValue(value)

	@property
	def parno(self):
		return self._parno

	@parno.setter
	def parno(self,value):
		if value in (True,False):
			self._parno = value
		else:
			raise ex.InvalidValue(value)

	@property
	def tec(self):
		return self._tec

	@tec.setter
	def tec(self,value):
		if value in (True,False):
			self._tec = value
		else:
			raise ex.InvalidValue(value)

	@property
	def description(self):
		return self._description

	@description.setter
	def description(self,value):
		self._description = value

class House(Property):

	def __init__(self,info_dict):

		Property.__init__(self,info_dict)
		self._floors = info_dict['floors']

	def get_info(self):
		to_return = Property.get_info(self)
		to_return['floors'] = self.floors
		return to_return

	@property
	def floors(self):
		return self._floors

	@floors.setter
	def floors(self,value):
		if isinstance(value,int):
			self.floors = value
		else:
			raise ex.InvalidValue(value)

class Apartment(Property):

	def __init__(self,info_dict):
		Property.__init__(self,info_dict)
		self._max_floors = info_dict['max_floors']
		self._floor = info_dict['floor']
		self._rooms = info_dict['rooms']

	def get_info(self):
		to_return = Property.get_info(self)
		to_return['max_floors'] = self.max_floors
		to_return['floor'] = self.floor
		to_return['rooms'] = self.rooms

	@property
	def floor(self):
		return self._floor

	@floor.setter
	def floor(self,value):
		if isinstance(value,int):
			self._floor = value
		else:
			raise ex.InvalidValue(value)

	@property
	def max_floors(self):
		return self._max_floors

	@max_floors.setter
	def max_floors(self,value):
		if isinstance(value,int):
			self._max_floors = value
		else:
			raise ex.InvalidValue(value)

	@property
	def rooms(self):
		return self._rooms

	@rooms.setter
	def rooms(self,value):
		if isinstance(value,int):
			self._rooms = value
		else:
			raise ex.InvalidValue(value)


class Properties(object):

	def __init__(self):

		self._filename = 'database'
		self.start_database()

	def start_database(self):
		database = shelve.open(self._filename)
		if database:
			self.rent_houses = database['rent_houses']
			self.sale_houses = database['sale_houses']
			self.rent_apartments = database['rent_apartments']
			self.sale_apartments = database['sale_apartments']
		else:
			self.rent_houses = {}
			self.sale_houses = {}
			self.rent_apartments = {}
			self.sale_apartments = {}
		database.close()

	def stop_database(self):
		database = shelve.open(self._filename)
		database['rent_houses'] = self.rent_houses
		database['rent_apartments'] = self.rent_apartments
		database['sale_apartments'] = self.sale_apartments
		database['sale_houses'] = self.sale_houses
		database.close()

	def add_property(self,info_dict):
		if info_dict['house']:
			house = House(info_dict)
			if info_dict['for_sale']:
				self.sale_houses[house.idd] = house
			else:
				self.rent_houses[house.idd] = house
		else:
			apartment = Apartment(info_dict)
			if info_dict['for_sale']:
				self.sale_apartments[apartment.idd] = apartment
			else:
				self.rent_apartments[apartment.idd] = apartment

	def remove_property(self,idd):
		str_key = str(idd)
		if str_key.startswith('1'):
			self.rent_houses.pop(idd)
		elif str_key.startswith('2'):
			self.sale_houses.pop(idd)
		elif str_key.startswith('3'):
			self.rent_apartments.pop(idd)
		elif str_key.startswith('4'):
			self.sale_apartments.pop(idd)

	def get_houses(self):
		to_return = self.rent_houses.update(self.sale_houses)
		return to_return

	def get_apartments(self):
		to_return = self.rent_apartments.update(self.sale_apartments)
		return to_return

	def get_all(self):
		to_return = self.rent_houses
		to_return.update(self.rent_apartments)
		to_return.update(self.sale_apartments)
		to_return.update(self.sale_houses)
		return to_return
