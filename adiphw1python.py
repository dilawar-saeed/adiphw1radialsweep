from PIL import Image

# load image
image_path = r'C:\Users\ds_sa\Desktop\Fall 23\ADIP\HW1\square.bmp'
image = Image.open(image_path)

# get dimensions (lenght and width)
x,y = image.size

starting_pixel = []    #first white pixel (will also be a boundary pixel always)
starting_pixel_found = 0   #bool variable to help terminate the loop that finds the first pixel
boundary = []               #list of all boundary pixels found

# nested loops to find first white pixel
for i in range(x):
    for j in range(y):
        intensity = image.getpixel((i,j))
        if (intensity == 255):          
            starting_pixel.append(i)                #find starting pixel coordinates
            starting_pixel.append(j)                
            boundary.append(starting_pixel)         #add to boundary list
            starting_pixel_found = 1
            break                                   #break inner loop
    if(starting_pixel_found == 1):                  #break outer loop
        break
            
current_pixel = starting_pixel      #the pixel on which radial sweep will be applied
temp_pixel = [0,0]                  #temporary pixel (neighbour of current pixel and potential candidate for next current_pixel hence radial sweep) 

start = 0       #int variable to keep track of which pixel to start next radial sweep on

while(temp_pixel != starting_pixel):                    #repeat till we circle back to original pixel
    
    #n8 neighbours of current pixel (starting_pixel in the first iteration)
    
    n8 = [[current_pixel[0]  ,current_pixel[1]-1],
        [current_pixel[0]-1,current_pixel[1]-1],
        [current_pixel[0]-1,current_pixel[1]],
        [current_pixel[0]-1,current_pixel[1]+1],
        [current_pixel[0]  ,current_pixel[1]+1],
        [current_pixel[0]+1,current_pixel[1]+1],
        [current_pixel[0]+1,current_pixel[1]],
        [current_pixel[0]+1,current_pixel[1]-1]]
    
    #print(n8)
    
    for i in range(len(n8)):        #iterate over all n8 neighbours of pixel
        
        # define temporary pixel from one of the predefined n8 neighbours and check for radial sweep conditions
        a = n8[start][0]            
        b = n8[start][1]
        temp_pixel = [a,b]          
        
        if(image.getpixel((a,b)) == 255):           #pixel must be white
            
            #pixel must have atleast one black neighbour
            if(image.getpixel((a+1,b)) == 0 or image.getpixel((a-1,b)) == 0 or image.getpixel((a,b-1)) == 0 or image.getpixel((a,b+1)) == 0):
                
                    start = (start+5)%8                 #setting correct direction for next radial sweep beginning
                    boundary.append(temp_pixel)         #add to boundary
                    current_pixel = temp_pixel          #update current pixel
                    break
                
                    # temp_pixel=boundary[len(boundary)-1]
                    # break
                    
            else:
                start = (start+1)%8             
                
        else:
            start = (start+1)%8
                

#print(boundary)

# converting original binary image to RGB
rgb_image = image.convert("RGB")

# setting all boundary pixels green
for pixel in boundary:
    rgb_image.putpixel((pixel[0], pixel[1]), (0,255,0))
rgb_image.show()




# UNCOMMENT TO DISPLAY BOUNDARY ONLY
#
#
# boundary_image = Image.new('L', (x, y), color=0)    # Initialize with all black pixels
# for pixel in boundary:                              # Set boundary pixels to white
#     boundary_image.putpixel((pixel[0], pixel[1]), 255)
# boundary_image.show()

