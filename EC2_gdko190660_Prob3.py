import random

def entrenar(theta,w1,w2,w3,epochs,x1,x2,res):
    error = True
    while error:
      error = False
      for i in range(0,5):
         fx = ((x1_init[i]*w_init[i])) + theta
         #print(fx)

         if fx >= 0:
            fx = 1
         else:
            fx = -1

         if fx != res[i]:
            error = True
            #calculo del error
            error = (res[i]-fx)
            #ajustar theta
            theta = theta+(res[i])
            #print(theta)
            #ajustar pesos
            w1 = w_init[i] + res[i] * x1_init[i]
            w2 = w_init[i] + res[i] * x1_init[i]
            w3 = w_init[i] + res[i] * x1_init[i]
            epochs +=1

    return w1,w2,w3,epochs,theta

#ciclo
if __name__=="__main__":
   epochs = 0
   x1_init=[0,1,2,2,3,4]
   x2_init=[2,4,4,0,1,1]
   w_init=[-1,-0.5,0,0.5,1]
   theta_init=[-1,-0.5,0,0.5,1]
   theta = random.choice(theta_init)
   w1 = random.choice(w_init)
   w2 = random.choice(w_init)
   w3 = random.choice(w_init)
   x1 = random.choice(x1_init)
   x2 = random.choice(x2_init)
   res = [-1,-1,-1,1,1,1]
   w1,w2,w3,epochs,theta = entrenar(theta,w1,w2,w3,epochs,x1,x2,res)
   print("x1: ",x1)
   print("x2: ",x2)
   print("w1: ",w1)
   print("w2: ",w2)
   print("w3: ",w3)
   print("theta: ",theta)
   print("epochs: ",epochs)