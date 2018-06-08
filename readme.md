# test-with-gitflow
Pequeno projeto para testar uma nova organização de branchs e tags.

O objetivo do Git Flow é fornecer um processo de desenvolvimento de software, auxiliando no controle das versões que estão sendo desenvolvidas e as que estão em produção utilizando branchs e tags.

Os principais tipos de branchs são:
 - `develop`: Branch fixa com as funcionalidades mais recentes;
 - `master`: Branch fixa com a versão mais estável, mais próxima de produção;
 - `feature/XXX` ou `bugfix/XXX`: Branch criada para as novas implementações ou correções de erros. São feitas sempre a partir de `develop`;
 - `release/XXX`: Branch criada para finalizar o release e tags. São feitas sempre a partir de `develop`;
 - `hotfix/XXX`: Branch criada para resolver problemas críticos em produção que não pode esperar um novo release. Criado sempre a partir de `master`.


![Gitflow Workflow](/git-workflow.png)

## Principais comandos

### Atuar em uma nova história
Antes de mais nada, certifique-se de sincronizar o seu ambiente:

```sh
$ git fetch origin
$ git checkout develop
$ git pull origin develop
```

Uma vez na branch `develop`, vamos criar uma nova branch para atuar na história:
```sh
$ git checkout -b feature/VALM-999
```

Lembre-se sempre de criar a branch a partir de `develop` com o nome `feature/<código da história no JIRA>`.

Para concluir, compartilhe a sua branch no repositório remoto com o comando abaixo e abra uma PR (Pull Request) para análise do seu código:

```sh
$ git add .
$ git commit -m "Nova funcionalidade"
$ git push origin feature/VALM-999
```

> Nota do autor: Ideal que as aprovações das PR's ocorram no mesmo dia, o mais tardar no dia seguinte. Podemos pensar em estipular um horário fixo no dia para esta tarefa. Podemos, inclusive, automatizar uma tarefa no Jenkins que disponibiliza a versão em um ambiente (digamos, hybrissit) tão logo a PR seja aprovada.


### Fechando uma versão

Com objetivo de preparar uma versão para deploy em produção, vamos criar uma nova branch a partir de `develop` com o próximo número da versão. Isto ajuda a isolar a release, possiblitando a equipe continuar atuando nas melhorias para a próxima versão.

```sh
$ git checkout -b release/v1.0 
$ git push origin release/v1.0
```

Uma vez criada esta branch, deverá estar disponível em algum ambiente (digamos, va.homolog) para testes pela equipe de QA (inclusive testes regressivos).
Caso encontrado algum erro, atua-se na correção na própria branch e, terminado, compartilha no repositório remoto e disponibiliza novamente no ambiente de testes:

```sh
$ git add .
$ git commit -m "Nova funcionalidade"
$ git push origin release/v1.0
```

Uma vez passada a fase de testes, para disponibilizar no ambiente de produção, deverá ser feito o merge com a branch `master` e criada a tag:

```sh
$ git checkout master 
$ git merge release/v1.0
$ git tag -a v1.0 “Release da versão 1.0”
$ git push v1.0
```

Uma vez em master, está pronto para disponibilizar no ambiente de produção.

> Nota do autor: O merge nesta etapa pode ser manual ou por meio de PR. Seria interessante disponibilizar esta versão também em um ambiente para testes futuros (digamos, hybrissitlm). 

Esta versão também necessita ser mergeado com a versão de desenvolvimento:

```sh
$ git checkout develop 
$ git merge release/v1.0
```


### Corrindo um erro em produção

Caso haja um erro crítico em produção e que não haja tempo hábil para aguardar o próximo release, o erro deverá ser corrigido em uma nova branch criada a partir de `master`: 

```sh
$ git checkout master
$ git pull origin master
$ git checkout -b hotfix/v1.1
```

Uma vez corrigido o erro, abra-se uma PR para `master`, com objetivo de aprovação do código alterado. Uma vez aprovado, uma nova versão de produção está pronta para deploy. Vamos criar uma tag para marcar a versão e disponibilizar a alteração também na branch `develop`:

```sh
$ git checkout master 
$ git tag -a v1.1 “Hotfix da versão 1.1”
$ git push v1.1
```

```sh
$ git checkout develop 
$ git merge hotfix/v1.1
```

## Referências

https://medium.com/trainingcenter/utilizando-o-fluxo-git-flow-e63d5e0d5e04
https://semver.org/


## Releases notes

### v2.0
  - Atualização do arquivo README

### v1.0
  - Criação do projeto e estrutura.