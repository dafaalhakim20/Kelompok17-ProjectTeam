import modulmodul as ic
import tkinter as tk 


main = tk.Tk()
main.state('zoomed')
main.title('RS UNS')
main.resizable(False,False)

page_check=0

if __name__=='__main__':
    ic.halaman1(main,page_check)
main.mainloop()
