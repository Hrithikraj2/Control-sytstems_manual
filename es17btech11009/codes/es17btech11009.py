
import control
import matplotlib.pyplot as plt

num = [0,0,1,3]
den = [1,-3,0,0]

#Transfer function GH = num/den
G = control.tf(num,den) 
control.nyquist(G)
plt.grid(True)
plt.title('Nyquist Diagram of G(s)H(s)')
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')
plt.show()



