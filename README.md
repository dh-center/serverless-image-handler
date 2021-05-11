
# Serverless Image Handler

Serverless image handler can save images to cloud storage (bucket), take it from the bucket and apply filters to it. This technology solves the problem with image storage. It can be quickly implemented in cloud service with a minimum amount of server resources. With these functions, you can optimize page load time and internet traffic. This is a solution for those who do not want to mess around with servers and distribute loads, but just start writing code for their project. 
## Authors

- [@nikmel2803](https://github.com/nikmel2803)
- [@ilyamore88](https://github.com/ilyamore88)
- [@DariaLoza](https://github.com/DariaLoza)
- [@julentiy](https://github.com/julentiy)
- [@marykorol98](https://github.com/marykorol98)


  
## Documentation

- [Yandex Cloud Function](https://cloud.yandex.ru/docs/functions/)
- [Python](https://www.python.org/doc/)
- [Boto3](https://cloud.yandex.ru/docs/storage/tools/boto)
- [Requests](https://docs.python-requests.org/en/master/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Terraform](https://www.terraform.io/docs/index.html)



  
![Logo](https://raw.githubusercontent.com/dh-center/serverless-image-handler/main/images/photo5429503918674653669.jpg)

    
## Demo

  https://images.dh-center.ru/index.html
## Deployment

Terraform deploying

  To deploy functions on Yandex Cloud with Terraform follow these steps:

1) Create terraform.tfvars file in terraform and fill it with variables like terraform.sample.tfvars
2) Run terraform apply command in terraform folder


  
## Filters

- crop
- blur
- resize
- pixelate
- optimize
- grey
- sepia
- negative
- noise
- brightness
- b&w



  