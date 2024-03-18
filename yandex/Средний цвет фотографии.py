from PIL import Image

image = Image.open('image.jpg')
pixels = image.load()
x, y = image.size
nums = [0, 0, 0]
for i in range(x):
    for j in range(y):
        nums = [pixels[i, j][k] + nums[k] for k in range(len(nums))]
print(*map(lambda n: n // x // y, nums))
