from SheetToDear.HTML.HTML import HTML as code

class Product:
    def __init__(self):
        self.our_id = None
        self.vendor_id = None
        self.brand = None
        self.gender = None
        self.product_name = None
        self.extra = None
        self.type = None
        self.material = None
        self.hardware = None
        self.outer_sole = None
        self.color = None
        self.made_in = None
        self.cost = None
        self.retail = None
        self.description = None
        self.sizes = dict()

    def set_our_id(self, our_id):
        self.our_id = str(our_id)

    def get_our_id(self):
        return "("+self.our_id+")"

    def set_vendor_id(self, vendor_id):
        self.vendor_id = str(vendor_id)

    def set_brand(self, brand):
        self.brand = str(brand)

    def set_gender(self, gender):
        self.gender = str(gender)

    def set_product_name(self, name):
        self.product_name = str(name)

    def set_extra(self, extra):
        self.extra = str(extra)

    def set_type(self, type):
        self.type = str(type)

    def set_material(self, material):
        self.material = str(material)

    def set_hardware(self, hardware):
        self.hardware = str(hardware)

    def set_outer_sole(self, outer_sole):
        self.outer_sole = str(outer_sole)

    def set_color(self, color):
        self.color = str(color)

    def set_made_in(self, made_in):
        self.made_in = str(made_in)

    def get_made_in(self):
        return "Made In "+self.made_in

    def set_cost(self, cost):
        self.cost = float(cost)

    def set_retail(self, retail):
        self.retail = float(retail)

    def add_size(self, size):
        size = str(float(size))
        if size in self.sizes:
            self.sizes[size] += 1
        else:
            self.sizes[size] = 1

    def set_description(self, description):
        self.description = description

    def get__description(self):
        result = code.ul(
            code.li(
                code.bold(
                    self.brand,
                    self.gender,
                    self.product_name,
                    self.extra,
                    self.color,
                    self.material,
                    self.type,
                    self.get_our_id()
                )
            ),
            code.li().addIf(
                code.bold("Material:"), not code.is_blank(self.material)
            ).addIf(
                self.material, code.is_blank(self.material)
            ),
            code.li(
                code.bold("Color:"),
                self.color
            ),
            code.li(
                code.bold("Outer Sole:"),
                self.outer_sole
            )
        )
        if (self.description is not None):
            result.add(code.li(
                self.description
            ))
        if (self.made_in is not None):
            result.add(code.li(
                self.get_made_in()
            ))
        result.add(code.li(
            code.bold(
                self.vendor_id
            )
        ))
        return result.export()


p = Product()
# p.set_brand('Mauri')
p.set_color('Black')
p.set_cost(200)
p.add_size(7.0)
p.set_made_in('Italy')
p.set_description('Desc Line')
p.set_extra('Cool')
p.set_gender("Men's")
p.set_hardware('Gold')
# p.set_material('Leather')
p.set_our_id('CPM2000')
p.set_outer_sole('Leather')
p.set_retail(500)
p.set_vendor_id(1000)
p.set_type('Loafers')
p.set_product_name('Great Shoe')

print(p.get__description())
