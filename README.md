<!--
*** O projeto desenvolvido se refere à disciplina de fundamentos de engenharia de software.
*** Demonstra um exemplo de interface desenvolvida em Python que simula as opções de cadastro para
*** uma empresa, armazenando os valores em outra aba, "lista".
-->

# :fax: Projeto de Simulação de Cadastro
<p align="center">
   <img src="https://img.shields.io/badge/Status-Concluído-blue"/>
</p>

## :sparkles: Características do projeto 
<p align="justify">Projeto em desenvolvimento para disciplina Fundamentos da Engenharia de Software do curso Talento Tech.
<br> O objetivo no projeto era uma apresentar uma interface de um sistema de cadastro teste que simula uma entrada para um banco de dados que poderia ser aplicado.
</p>
<!--
*** O cronograma do projeto pode ser observado pelas datas de commits e etc, sendo redundante elaborar sobre ao longo deste arquivo README.
-->
<img align="center" width="900" height="500" src="https://github.com/user-attachments/assets/037ac23c-5069-40a0-b8fd-54f6660c4f27" alt="Gif demonstrando um cadastro fictício">

## :notebook: Tecnologias utilizadas

<ul>
<li>O código foi desenvolvido na linguagem Python</li>
<li>Elaborado no VSCode</li>
<li>Biblioteca TKinter</li>
<li>Classes e classes abstratas</li>
</ul>

## :file_folder: Acesso ao projeto

<p><strong>Instruções para acessar o projeto </strong></p>

* Copie o repositório 
  ```sh
  git clone https://github.com/whironn/projeto-individual
  ```
  
* Certifique-se de ter Python instalado na sua máquina 
  ```sh
  python --version
  ```
  `Salve a pasta dos arquivos na sua máquina.` <br>
  `Se tudo foi operado corretamente, você deve ser capaz de rodar o código si mesmo.`
  

## :hammer: Funcionalidades
<p> :heavy_check_mark: A interface permite o cadastro de afiliados e classificação em "fornecedor" ou "comprador".</p>
<p> :heavy_check_mark: O cadastro requer o preenchimento de todos os atributos e a seleção é limitada à apenas um "Status" ou "Categoria".</p>
<p> :heavy_check_mark: Oferece opção de preenchimento de Nome, ID, Contato, Filial e Data de Emissão, que é armazenado na aba "lista". </p>
<p> :heavy_check_mark: Classificação de "status", simulando as pendencias, atrasos ou conclusões ao ser armazenado. </p>
<p> :heavy_check_mark: A aba "lista" oferece a opção de apagar um cadastro inserido, em caso de erros e etc. </p>


<!--
*** Abaixo segue a documentação do projeto realizado, com o processo de desenvolvimento, 
*** incluindo os desafios enfrentados e como o Git ajudou a gerenciar o projeto, tudo adicionado e presente no repositório.
-->
<details>
  <summary>Documentação</summary>
   
   # Nome do projeto
   <p> Projeto de Simulação de Cadastro </p>

   # Características
   <p align="justify"> Interface de cadastro desenvolvida em Python usando as bibliotecas ABC (abstract base class) e TKinter, composta por duas abas, "Cadastro de Afiliados" e "Lista", responsáveis por possibilitar o cadastro com atributos como "ID", "Filial", "Categoria", "Nome", "Status", "Data de emissão", "Contato", e por armazenar esses atributos de forma sintetizada, respectivamente. </p>

   # Processo, dificuldades e Git
   
  <p align="justify"> Ao longo do desenvolvimento, as etapas mais complexas foram a própria concepção da ideia do projeto, e em seguida a organização dos novos atributos para se encaixar no padrão do sistema desenvolvido e tornar a interface mais repleta, sendo necessário estudar e compreender a utilização da biblioteca TKinter, seguindo com a etapa que levou mais tempo e exigiu maior complexidade, a adição do simples botão "Apagar", onde se mostrou como um grande desafio exigindo maestria de grande parte do uso da biblioteca TKinter, mas tornou o uso da interface mais repleto.</p>
   <p>De mesma forma, o processo de desenvolvimento desse projeto foi muito beneficiado pelo uso de Git, que facilitou drasticamente manter os arquivos organizados e testar ao longo do tempo as "features" como o botão "Apagar" sem arriscar comprometer o código original, graças ao uso de branchs</p>
</details>



