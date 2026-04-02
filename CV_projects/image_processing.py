import streamlit as st
import cv2
import numpy as np

# Streamlit Page Setup
st.set_page_config(page_title='Radiant AI', page_icon='ai_icon.png',layout="wide")
st.markdown("## Radiant AI ✨")
st.markdown("#####  Mini Image Editing Dashboard")
st.divider()

# File Upload
uploaded_file = st.file_uploader("Upload your Image", type=["jpg", "jpeg", "png"])

# ---------- FILTER FUNCTIONS ---------- #

# Cool Tint (blue effect)
def apply_cool_tint(img):
    cool_img = img.copy()
    cool_img[:, :, 1] = cool_img[:, :, 1] // 3  # Reduce green
    cool_img[:, :, 2] = cool_img[:, :, 2] // 3  # Reduce red
    return cool_img

# Blue Tint
def apply_blue_tint(img):
    blue_img = img.copy()
    blue_img[:, :, 0] = cv2.add(blue_img[:, :, 0], 50)   # Enhance blue
    blue_img[:, :, 1] = blue_img[:, :, 1] // 4            # Reduce green
    blue_img[:, :, 2] = blue_img[:, :, 2] // 4            # Reduce red
    blue_img = np.clip(blue_img, 0, 255)
    return blue_img

# Light Red Tint (already defined)
def apply_lred_tint(img):
    lred_img = img.copy()
    lred_img[:, :, 0] = cv2.add(lred_img[:, :, 0], 50)   
    lred_img[:, :, 1] = lred_img[:, :, 1] // 4           
    lred_img[:, :, 2] = lred_img[:, :, 2] // 4           
    lred_img = np.clip(lred_img, 0, 255)
    return lred_img

# Sharpness Filter
def apply_sharpness(img):
    kernel = np.array([[0, -1, 0], 
                       [-1, 5,-1], 
                       [0, -1, 0]])  # Sharpening kernel
    sharp_img = cv2.filter2D(img, -1, kernel)
    return sharp_img

# Enhancement (Contrast Boost)
def enhance_image(img):
    enhanced_img = cv2.convertScaleAbs(img, alpha=1.5, beta=30)  # Increase contrast and brightness
    return enhanced_img

# Apply Sepia
def apply_sepia(img):
    sepia_filter = np.array([[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]])
    sepia_img = cv2.transform(img, sepia_filter)
    sepia_img = np.clip(sepia_img, 0, 255)
    return sepia_img

def apply_cartoon_effect(img):
    # Step 1: Convert to grayscale
    cart_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray_cart = cv2.cvtColor(cart_img, cv2.COLOR_BGR2GRAY)
    smoothGrayScale = cv2.medianBlur(gray_cart, 5)
    getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255, 
      cv2.ADAPTIVE_THRESH_MEAN_C, 
      cv2.THRESH_BINARY, 9, 9)
    colorImage = cv2.bilateralFilter(cart_img, 9, 300, 300)
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)
    return cartoonImage

def apply_cartoon_effect_better(img):
    # Resize for speed
    img = cv2.resize(img, (600, int(img.shape[0] * 600 / img.shape[1])))

    # Step 1: Edge detection (using Canny for crisp lines)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, 5)
    edges = cv2.Canny(gray_blur, 100, 200)

    # Optional: Thicken edges
    kernel = np.ones((2, 2), np.uint8)
    edges_dilated = cv2.dilate(edges, kernel, iterations=1)

    # Step 2: Color quantization using k-means
    data = np.float32(img).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.5)
    _, labels, centers = cv2.kmeans(data, 6, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    quantized = centers[labels.flatten()].reshape(img.shape).astype(np.uint8)

    # Step 3: Bilateral Filter to smooth colors (preserving edges)
    smooth = cv2.bilateralFilter(quantized, d=9, sigmaColor=150, sigmaSpace=150)

    # Step 4: Combine edges with smoothed color
    cartoon = cv2.bitwise_and(smooth, smooth, mask=255 - edges_dilated)

    return cartoon


def apply_anime_effect(img):
    # 1. Bilateral Filter to smooth colors while keeping edges
    smooth = cv2.bilateralFilter(img, d=9, sigmaColor=150, sigmaSpace=150)

    # 2. Convert to grayscale and apply median blur
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 7)

    # 3. Detect edges
    edges = cv2.adaptiveThreshold(blur, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

    # 4. Reduce color palette (color quantization)
    data = np.float32(smooth).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    _, labels, centers = cv2.kmeans(data, 8, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    quantized = centers[labels.flatten()].reshape(img.shape)

    # 5. Combine edges with color-quantized image
    anime = cv2.bitwise_and(quantized, quantized, mask=edges)

    return anime

def apply_stylized_cartoon(img):
    return cv2.stylization(img, sigma_s=60, sigma_r=0.45)

def apply_oil_painting(img):
    return cv2.xphoto.oilPainting(img, 7, 1)

def apply_watercolor(img):
    return cv2.stylization(img, sigma_s=60, sigma_r=0.6)

def apply_hdr(img):
    return cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)

def invert_colors(img):
    return cv2.bitwise_not(img)

def apply_warm_filter(img):
    warm_img = img.copy()
    warm_img[:, :, 2] = cv2.add(warm_img[:, :, 2], 40)
    warm_img[:, :, 1] = cv2.add(warm_img[:, :, 1], 20)
    return np.clip(warm_img, 0, 255)

def apply_cold_filter(img):
    cold_img = img.copy()
    cold_img[:, :, 0] = cv2.add(cold_img[:, :, 0], 30)
    cold_img[:, :, 2] = cv2.subtract(cold_img[:, :, 2], 20)
    return np.clip(cold_img, 0, 255)








# ---------- MAIN APP ---------- #

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    st.image(image, channels="BGR", caption="Uploaded Image", width=400)
    #sharped_img = apply_sharpness(image)
    #st.image(cv2.cvtColor(sharped_img, cv2.COLOR_BGR2RGB), caption="Sharpened Image", width=400)


    col1a, col2a, col3a = st.columns((1,1,1))
    with col1a:
        sharped_img = apply_sharpness(image)
        #st.image(sharped_img, caption="Sharped Image", width=300)
        st.image(cv2.cvtColor(sharped_img, cv2.COLOR_BGR2RGB), caption="Sharpened Image", width=300)
    with col2a:
        hdr_style = apply_hdr(image)
        st.image(cv2.cvtColor(hdr_style, cv2.COLOR_BGR2RGB), caption='HDR Style', width=300)
        
    with col3a:
        #cartoon_img = apply_cartoon_effect_better(image)
        #st.image(cv2.cvtColor(cartoon_img, cv2.COLOR_BGR2RGB), caption="Cartoon Effect", width=300)
        #anime_img = apply_anime_effect(image)
        #st.image(cv2.cvtColor(anime_img, cv2.COLOR_BGR2RGB), caption="Anime Effect", width=300)
        enhanced_img = enhance_image(image)
        #st.image(enhanced_img, caption="Enhanced Contrast", width=300)
        st.image(cv2.cvtColor(enhanced_img, cv2.COLOR_BGR2RGB), caption="Enhanced Contrast", width=300)




    # Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Black and White
    _, bw = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    # Pencil Sketch
    inv_img = 255 - gray_image
    blur_img = cv2.GaussianBlur(inv_img, (21, 21), 0)
    inv_blur = 255 - blur_img
    sketch = cv2.divide(gray_image, inv_blur, scale=256.0)

    # Red Tint
    red_tint = image.copy()
    red_tint[:, :, 1] = 0  # Remove green
    red_tint[:, :, 2] = 0  # Remove red

    # Cool Tint
    cool_tint = apply_cool_tint(image)

    # Light Red Tint
    lred_tint = apply_lred_tint(image)

    # Edge Detection and Morphology 
    canny_edge = cv2.Canny(gray_image,100,200)
    # Sobel kernel for horizontal edges (Gx)
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    # -> Sobel kernel for vertical edges (Gy)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    # ->  Compute the magnitude of the gradient (edge strength)
    magnitude = cv2.magnitude(sobel_x, sobel_y)
    # -> Convert the result to 8-bit (for display)
    magnitude = np.uint8(np.absolute(magnitude))   
    # Morphology
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(gray_image, kernel, iterations=2) 
    eroded = cv2.erode(gray_image, kernel, iterations=2)
    opening = cv2.morphologyEx(gray_image, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(gray_image, cv2.MORPH_CLOSE, kernel)

    # ---------- DISPLAY FILTERED IMAGES ---------- #

    col16, col17, col18 = st.columns(3)
    with col16:
        warm_style = apply_warm_filter(image)
        st.image(cv2.cvtColor(warm_style, cv2.COLOR_BGR2RGB), caption="Warm Style", width=300)
    with col17:
        cold_style = apply_cold_filter(image)
        st.image(cold_style, caption='Cold Style', width= 300)
        #st.image(cv2.cvtColor(warm_style, cv2.COLOR_BGR2RGB), caption="Cold Style", width=300)    
    with col18:
        warm_style2 = apply_warm_filter(image)
        st.image(warm_style2, caption='Blue Tint', width= 300)
        #st.image(cv2.cvtColor(warm_style, cv2.COLOR_BGR2RGB), caption="Warm Style", width=300)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(gray_image, caption="Grayscale", width=300)
    with col2:
        st.image(bw, caption="Black & White", width=300)
    with col3:
        st.image(sketch, caption="Pencil Sketch", width=300)

    col4, col5, col6 = st.columns(3)
    with col4:
        st.image(red_tint, caption="Red Tint", width=300)
    with col5:
        st.image(cool_tint, caption="Cool Tint", width=300)
    with col6:
        st.image(lred_tint, caption="Light Red Tint", width=300)

    col7, col8, col9 = st.columns(3)
    with col7:
        st.image(canny_edge, caption="Canny Edge", width=300)
    with col8:
        st.image(magnitude, caption="Sobel Edge", width=300)
    with col9:
        st.image(dilated, caption="Dilated Morphology", width=300)
    
    col10, col11, col12 = st.columns(3)
    with col10:
        st.image(eroded, caption="Eroded Morphology", width=300)
    with col11:
        st.image(opening, caption="Opening Morphology", width=300)
    with col12:
        st.image(closing, caption="Closed Morphology", width=300)

    col13, col14, col15 = st.columns(3)
    with col13:
        oil_style = apply_oil_painting(image)
        st.image(cv2.cvtColor(oil_style, cv2.COLOR_BGR2RGB), caption="Oil Style", width=300)
    with col14:
        water_style = apply_watercolor(image)
        st.image(cv2.cvtColor(water_style, cv2.COLOR_BGR2RGB), caption='Water Style', width=300)
    with col15:
        invert_img = invert_colors(image)
        st.image(invert_img, caption='Invert Style',width=300)
        #st.image(cv2.cvtColor(invert_img, cv2.COLOR_BGR2RGB), caption="Invert Style", width=300)

    

    
    

