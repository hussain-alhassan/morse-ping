### Vulnerability
If packets are manipulated to be sent at certain times, this can be used for purposes of sending communications undetected in a way similar to Morse Code. An eavesdropper would be more likely to focus on the information the packets contain, rather than the timing between the packets, to decipher any secret messages. This method of communication is similar to steganography in that the actual message is not encrypted (other than being converted into some sort of non-numeric or non-alphabetic form), but rather the fact that the communication is happening at all is made to be undetectable.
### How it works
The project will consist of two different programs: a client and a server. Our project will send packets (neither the size of the packets nor the information contained within are relevant) from one computer to another computer. The message that will be sent will not be contained in the packets, but in the time delay between the sending of the packets. Therefore, the information in the packets will not matter other than to potentially use for the deception or misdirection of potential listeners. It is similar to morse code in that the packets act as the sound tone used to relay the message and the delay between the packets are the equivalent of the length of the tone (dots and dashes).

The programs will be written in Python, and will use GUIs. The client will take a message the user types into a GUI text box, convert it to binary, then send it to the server over UDP when the user clicks on a button, encoding the information in the delay between packets. A very small or no delay between two packets will represent a 0, and a long delay between packets will represent a 1. There will be a flat, constant delay between each group of 2 packets. The server program will receive the packets, and measure the time delays between packets reconstructing the message in binary form. The message will be converted from binary to plaintext and displayed on the screen for the  recipient user.
### Usage
* Clone the project.
* Navigate to the project.
* Open 2 terminal windows.
* On the first window, run this command.
`python server.py`

* Then on the second window, run this command
`python client.py`
* A window will pop up. Enter a message and watch the server window.

### End