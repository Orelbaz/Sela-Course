provider "aws" {
  region = "eu-central-1"
}

resource "aws_instance" "test" {
  ami           = "ami-0e00e602389e469a3"
  instance_type = "t2.micro"

  tags = {
    Name = "test-compose-TF"
  }

  key_name = "or"

  vpc_security_group_ids = ["sg-019220316a7d95404"]

  provisioner "file" {
    source      = "docker-compose.yml"
    destination = "/home/ec2-user/docker-compose.yml"
  }  
  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo yum install docker -y",
      "sudo curl -L \"https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)\" -o /usr/local/bin/docker-compose",
      "sudo chmod +x /usr/local/bin/docker-compose",
      "sudo systemctl enable docker",
      "sudo systemctl start docker",
      "cd /home/ec2-user/Sela-Course/Terraform",
      "sudo docker-compose up -d"
    ]

    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("/home/or/Desktop/PrivateKeys/or.pem")
      host        = self.public_ip
    }
  }
}
