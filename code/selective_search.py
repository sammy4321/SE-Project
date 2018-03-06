import skimage.data
import selectivesearch

img = skimage.data.astronaut()
img_lbl, regions = selectivesearch.selective_search(img, scale=500, sigma=0.9, min_size=10)

