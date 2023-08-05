# import the important module in python
import numpy as np
			
# make matrix with numpy
gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')
			
# applying matrix.take() method
geek = gfg.take(0, 1)
	
print(geek)
