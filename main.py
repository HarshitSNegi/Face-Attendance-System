import tkinter as tk
import cv2

class App:
    def __init__(self):
        self.main_window = tk.Tk() #creating a window here Tk is a variable representing window
        self.main_window.geometry("1200x530+350+100") #size of our window above- x and y location
        
        

        self.login_button_main_window = util.get_button(self.main_window, "Login", 20, 2, self.login_window)#creating a button for login and calling the function login_window when the button is clicked. util.get_button is a function that creates a button with the specified parameters and returns it. The parameters are the parent window, the text on the button, the font size, the padding, and the command to be executed when the button is clicked.
        self.login_button_main_window.place(x=750, y=300)

        self.register_new_user_button_main_window = util.get_button(self.main_window, 'register new user', 'gray',
                                                                    self.register_new_user, fg='black') #creating a button for registering a new user and calling the function register_new_user when the button is clicked. The parameters are the parent window, the text on the button, the background color, the command to be executed when the button is clicked, and the foreground color.)
        self.register_new_user_button_main_window.place(x=750, y=400)#placing the button at the specified x and y coordinates on the main window. The place method is used to position the button at an absolute location on the window, rather than using a layout manager like pack or grid.
        
        self.webcam_label = util.get_img_label(self.main.window)
        self.webcam_label.place(x=50, y=50, width=700, height=500) #creating a label for displaying the webcam feed and placing it at the specified x and y coordinates on the main window. The width and height parameters specify the size of the label.

        self.add_webcam(self.webcam_label) #calling the add_webcam function to start the webcam feed and display it on the label. The add_webcam function is responsible for capturing the webcam feed and updating the label with the video frames.
        
def add_webcam(self, label): #the add_webcam function is responsible for capturing the webcam feed and updating the label with the video frames. The function takes a label as a parameter, which is used to display the webcam feed. The function can be implemented using OpenCV to capture the video feed from the webcam and update the label with the video frames.
    if 'cap'_not in self,__dict__: #checking if the cap attribute is not already defined in the instance. This is done to ensure that we only create a VideoCapture object once and reuse it for subsequent calls to the add_webcam function.
    self.cap = cv2.VideoCapture(0) #creating a VideoCapture object to capture the video feed from the webcam. The parameter 0 specifies that we want to capture from the default webcam. If you have multiple webcams, you can specify the index of the webcam you want to use (e.g., 1 for the second webcam).
       
    self._label = label

    self.process_webcam()

def process_webcam(self):#the process_webcam function is responsible for capturing the video feed from the webcam, processing the video frames, and updating the label with the processed video frames. The function can be implemented using OpenCV to capture the video feed, perform any necessary processing (e.g., face recognition), and update the label with the processed video frames. The function can be called in a loop to continuously update the webcam feed on the label.
    ret, frame = self.cap.read() #capturing a frame from the webcam feed using the read method of the VideoCapture object. The ret variable indicates whether the frame was successfully captured, and the frame variable contains the captured video frame.

def login(self):
        pass
 
def register_new_user(self):   #creating a new window for registering a new user when the register new user button is clicked. The function is called when the register new user button is clicked and it creates a new window for registering a new user. The function is currently empty and can be implemented to create the register new user window and its functionality.
        pass
     

if __name__=="__main__":
    app=App()
    app.start()


