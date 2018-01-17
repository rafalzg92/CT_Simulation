 
import numpy as np
from scipy import misc



def New_image(input_image):
    threshold = 128

    img = misc.imread(input_image)


    if (img.shape[0] > img.shape[1]):
        dim = img.shape[1]
    elif (img.shape[0] < img.shape[1]):
        dim = img.shape[0]
    else:
        dim = img.shape[0]
    

    img2 = np.zeros((dim, dim), dtype = np.uint8)


    for i in xrange(dim):
        for j in xrange(dim):
            if (len(img.shape) > 2):
                img2[i,j] = int(np.average(img[i,j]))
            else:
                img2[i,j] = img[i,j]

            if (img2[i,j] < threshold):
                img2[i,j] = 0
            else: 
                img2[i,j] = 255
                
    X = []
    X.append(img2)
    X.append(dim)
    return X







def Xray(img, x1, y1, angle, TAB):
    alpha1 = 100
    alpha2 = 0
    if (angle <= 90):
        if (angle >= 45):
            angle = np.radians(angle)
        else:
            alpha1 = angle
            angle = 90 - angle
            angle = np.radians(angle)
            img = np.transpose(img)
            (x1, y1) = (y1, x1)

        if (len(img) - x1 > np.tan(angle) * (len(img) - y1)):
            y2 = len(img) - 1
            x2 = np.tan(angle) * (y2 - y1) + x1
            x2 = int(round(x2))
        else:
            x2 = len(img) - 1
            y2 = (x2 - x1) / np.tan(angle) + y1
            y2 = int(round(y2))
    else:
        angle = angle - 90
        if (angle <= 45):            
            angle = np.radians(angle)
        else:
            alpha2 = angle
            angle = 90 - angle
            angle = np.radians(angle)
            img = np.transpose(np.fliplr(np.flipud(img)))
            (x1, y1) = (len(img) - y1 - 1, len(img) - x1 - 1)
            
            
        if (len(img) - x1 > y1 / np.tan(angle)):
            y2 = 0
            x2 = y1 / np.tan(angle) + x1
            x2 = int(round(x2))
        else:
            x2 = len(img) - 1
            y2 = y1 - np.tan(angle) * (len(img) - x1 - 1)
            y2 = int(round(y2))
            
    if (x2 > len(img) - 1):
        x2 = len(img) - 1
    if (y2 > len(img) - 1):
        y2 = len(img) - 1
    
    suma = 0
    
    if (x1 < x2):
        xi = 1
        dx = x2 - x1
    else:
        xi = -1
        dx = x1 - x2
    
    if (y1 < y2):
        yi = 1
        dy = y2 - y1
    else:
        yi = -1
        dy = y1 - y2
        
    if (img[x1,y1] == 0):
        suma = suma + 1

    x = x1
    y = y1

    if (dx > dy):
        ai = (dy - dx) * 2
        bi = dy * 2
        d = bi - dx
    
        while (x != x2):
            if (d >= 0):
                x = x + xi
                y = y + yi
                d = d + ai
            else:
                d = d + bi
                x = x + xi
            if (img[x,y] == 0):
                suma = suma + 1
        
    else:
        ai = (dx - dy) * 2
        bi = dx * 2
        d = bi - dy
    
        while (y != y2):
            if (d >= 0):
                x = x + xi
                y = y + yi
            else:
                d = d + bi
                y = y + yi
            if (img[x,y] == 0):
                suma = suma + 1
                
    TAB.append(suma)
    
    if (alpha1 < 45): 
        img = np.transpose(img)  
    if (alpha2 > 45):
        img = np.transpose(np.fliplr(np.flipud(img)))







def Draw(img, x1, y1, angle, val):
    alpha1 = 100
    alpha2 = 0
    if (angle <= 90):
        if (angle >= 45):
            angle = np.radians(angle)
        else:
            alpha1 = angle
            angle = 90 - angle
            angle = np.radians(angle)
            img = np.transpose(img)
            (x1, y1) = (y1, x1)

        if (len(img) - x1 > np.tan(angle) * (len(img) - y1)):
            y2 = len(img) - 1
            x2 = np.tan(angle) * (y2 - y1) + x1
            x2 = int(round(x2))
        else:
            x2 = len(img) - 1
            y2 = (x2 - x1) / np.tan(angle) + y1
            y2 = int(round(y2))
    else:
        angle = angle - 90
        if (angle <= 45):            
            angle = np.radians(angle)
        else:
            alpha2 = angle
            angle = 90 - angle
            angle = np.radians(angle)
            img = np.transpose(np.fliplr(np.flipud(img)))
            (x1, y1) = (len(img) - y1 - 1, len(img) - x1 - 1)
            
            
        if (len(img) - x1 > y1 / np.tan(angle)):
            y2 = 0
            x2 = y1 / np.tan(angle) + x1
            x2 = int(round(x2))
        else:
            x2 = len(img) - 1
            y2 = y1 - np.tan(angle) * (len(img) - x1 - 1)
            y2 = int(round(y2))
            
    if (x2 > len(img) - 1):
        x2 = len(img) - 1
    if (y2 > len(img) - 1):
        y2 = len(img) - 1
    
    
    if (x1 < x2):
        xi = 1
        dx = x2 - x1
    else:
        xi = -1
        dx = x1 - x2
    
    if (y1 < y2):
        yi = 1
        dy = y2 - y1
    else:
        yi = -1
        dy = y1 - y2
        
    img[x1,y1] = val

    x = x1
    y = y1

    if (dx > dy):
        ai = (dy - dx) * 2
        bi = dy * 2
        d = bi - dx
    
        while (x != x2):
            if (d >= 0):
                x = x + xi
                y = y + yi
                d = d + ai
            else:
                d = d + bi
                x = x + xi
            img[x,y] = val
        
    else:
        ai = (dx - dy) * 2
        bi = dx * 2
        d = bi - dy
    
        while (y != y2):
            if (d >= 0):
                x = x + xi
                y = y + yi
            else:
                d = d + bi
                y = y + yi
            img[x,y] = val
                
    
    if (alpha1 < 45): 
        img = np.transpose(img)  
    if (alpha2 > 45):
        img = np.transpose(np.fliplr(np.flipud(img)))
    
    return img







def Scan(space, delta_angle, img):
    Profiles = []
    Angles = []

    for angle in xrange(180):
        if (angle % delta_angle == 0):
            Angles.append(angle)
    
    for angle in Angles:
    
        T0 = []
        T1 = []
        T2 = []    
        TAB = []
    
        for i in xrange(len(img)):   
            if (angle == 0 or angle == 90):
                if (i % space == 0):
                    T0.append(i)
            else:
                space1 = space / np.sin(np.radians(90 - angle))
                space1 = int(round(space1))
                if (i % space1 == 0):
                    T1.append(i)
                space2 = space / np.sin(np.radians(angle))
                space2 = int(round(space2))
                if (i % space2 == 0):
                    T2.append(i)
        
    
        if (angle == 0):
            T0.reverse()
            for i in T0:
                x1 = i
                y1 = 0
                Xray(img, x1, y1, angle, TAB)
        elif (angle == 90):
            for i in T0:
                x1 = 0
                y1 = i
                Xray(img, x1, y1, angle, TAB)
        elif (angle < 90):
            T1.reverse()
            for i in T1:
                x1 = i
                y1 = 0
                Xray(img, x1, y1, angle, TAB)
            for i in T2:
                if (i == 0):
                    continue
                x1 = 0
                y1 = i
                Xray(img, x1, y1, angle, TAB)
        else:
            r = len(img) - 1 - max(T2)
            for i in T2:
                i = i + r
                if (i == len(img) - 1):
                    break
                x1 = 0
                y1 = i
                Xray(img, x1, y1, angle, TAB)
            for i in T1:
                x1 = i
                y1 = len(img) - 1
                Xray(img, x1, y1, angle, TAB)
            
        Profiles.append(TAB)
    
        print angle
        print TAB
        print "==============================================="
    
    return Profiles
 
 
 
 



def Back_projection(Profiles, dim, space, delta_angle, result):
    
    
    
    Angles = []

    for angle in xrange(180):
        if (angle % delta_angle == 0):
            Angles.append(angle)
    
    Images = []

    N = 0
    for angle in Angles:
    
        T0 = []
        T1 = []
        T2 = []
        img = np.zeros((dim,dim), dtype = np.int)
    
        for i in xrange(len(img)):   
            if (angle == 0 or angle == 90):
                if (i % space == 0):
                    T0.append(i)
            else:
                space1 = space / np.sin(np.radians(90 - angle))
                space1 = int(round(space1))
                if (i % space1 == 0):
                    T1.append(i)
                space2 = space / np.sin(np.radians(angle))
                space2 = int(round(space2))
                if (i % space2 == 0):
                    T2.append(i)
        n = 0
        if (angle == 0):
            T0.reverse()
            for i in T0:
                if (Profiles[N][n] > 0):
                    x1 = i
                    y1 = 0
                    Draw(img, x1, y1, angle, Profiles[N][n])
                n = n + 1
        elif (angle == 90):
            for i in T0:
                if (Profiles[N][n] > 0):
                    x1 = 0
                    y1 = i
                    Draw(img, x1, y1, angle, Profiles[N][n])
                n = n + 1
        elif (angle < 90):
            T1.reverse()
            for i in T1:
                if (Profiles[N][n] > 0):
                    x1 = i
                    y1 = 0
                    Draw(img, x1, y1, angle, Profiles[N][n])
                n = n + 1
            for i in T2:
                if (i == 0):
                    continue
                if (Profiles[N][n] > 0):
                    x1 = 0
                    y1 = i
                    Draw(img, x1, y1, angle, Profiles[N][n])
                n = n + 1
        else:
            r = len(img) - 1 - max(T2)
            for i in T2:
                i = i + r
                if (i == len(img) - 1):
                    break
                if (Profiles[N][n] > 0):
                    x1 = 0
                    y1 = i
                    Draw(img, x1, y1, angle, Profiles[N][n])
                n = n + 1
            for i in T1:
                if (Profiles[N][n] > 0):
                    x1 = i
                    y1 = len(img) - 1
                    Draw(img, x1, y1, angle, Profiles[N][n])
                n = n + 1  
        Images.append(img)        
        N = N + 1
            
    image = sum(Images)
    pict = np.zeros((dim, dim), dtype = np.uint8)
    
    for i in xrange(dim):
        print i, "/", dim - 1
        for j in xrange(dim):
            pict[i,j] = int(round(255.0 * (image[i,j] - np.max(image)) / (np.min(image) - np.max(image))))
            
    print image
    print np.max(image)
    print np.min(image)    
    print pict
            
    misc.imsave(result, pict)


        
        
        
        
        
space = 1
delta_angle = 1
input_image = "lorem.jpg"
output_image = "lorem1.jpg"



T = New_image(input_image)
img = T[0]
dim = T[1]
Profiles = Scan(space, delta_angle, img)
Back_projection(Profiles, dim, space, delta_angle, output_image)
