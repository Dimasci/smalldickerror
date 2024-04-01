import ctypes
import winsound

# Define constants for MessageBox
MB_ICONERROR = 0x00000010
MB_YESNO = 0x00000004

while True:
    # Display a message box with Yes and No options
    response = ctypes.windll.user32.MessageBoxW(0, "Windows обнаружила что ваш член очень маленький. Это так?", "Error", MB_YESNO | MB_ICONERROR)

    # Check the user's response
    if response == 6:  # 6 corresponds to the 'Yes' button
        print("User clicked 'Yes'")
        break  # Exit the loop if 'Yes' is clicked
    else:
        print("User clicked 'No' or closed the window")
        # Play error sound
        winsound.MessageBeep(winsound.MB_ICONHAND)
