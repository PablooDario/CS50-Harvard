from fpdf import FPDF

class PDF(FPDF):
    
    def header(self):
        self.set_font("helvetica", "B", 50)
        self.cell(0, 10, "CS50 Shirtificate", align="C")

    def shirt(self, name):
        image_path = "./shirtificate.png"
        self.image(image_path, x=32, y=50, w=150)
        self.set_font("helvetica", "B", 15)
        
        self.set_y(90)
        self.set_text_color(255, 255, 255)
        self.set_x(25)
        self.cell(0, 10, f"{name} took CS50", align='C')

        self.set_fill_color(r=255, g=255, b=255)
        self.star(x=95, y=130, r_in=5, r_out=15, rotate_degrees=0, corners=3, style="FD")
        self.star(x=125, y=130, r_in=5, r_out=15, rotate_degrees=0, corners=3, style="FD")
        self.star(x=110, y=155, r_in=5, r_out=15, rotate_degrees=0, corners=3, style="FD")

def main():
    pdf = PDF()
    pdf.add_page() 
    name = input("Name: ")
    pdf.shirt(name)
    pdf.output("shirtificate.pdf")



if __name__ == "__main__":
    main()