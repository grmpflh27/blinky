### build
docker build -t python-cv2-jupyterlab:latest .

### run

docker run -v `pwd`:/code -p 8888:8888 python-cv2-jupyterlab:latest  