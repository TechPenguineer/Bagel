<p align="center">
<img src="./img/logopng.png">
<h1 align="center">Bagel</h1> 
</p>
<h3 align="center"><b>The Bagel language is a simple language that is used to create an advanced, stylistic, and reactive web pages</h3>
<br><br>

# 📖 Table Of Contents

- [» Introduction](#👋-introduction)
- - [» How To Use](#🤔-how-to-use)
- [» Syntax](#☁️-syntax)
-  [» Install](#🔽-download)

# 👋 Introduction
Bagel is the newest and best transpiled web development language. Bagel is aimed to be organized, clean, minimal, and supports all sub-languages such as *JS*, *CSS*, and *HTML*. Bagel when built is made into a singular file. 

<br><br>
 
# 🤔 How To Use
Bagel has a built in interperter. The CLI trigger word is `bagel`. You can run `bagel build <file>` to transpiled to HTML. You can also run `bagel help`. 

<br><br>

# ☁️ Syntax
## Setting Window Properties 
`-$` will identify that youre changing a window property

Property Types include:<br>
`ico`, `title`, and soon to be `theme`

### Example
Setting Title:

```-$ title = Hello World```

Setting Icon

```-$ ico = % ./img/icon.png```

the `%` signifys youre working with a directory and not a url


# 🔽 Download

<p align="center">There is no download avaliable at this time</p>

# ⌛ TODO
- [x] Comment Lines
- [x] Window Properties
- [x] Main lexer system
- [x] Parser
- [x] Build Command
- [ ] Align `.bagl` file lines to `.html` lines. Example:

## Currently: 

**.bagl**

`
-$ title = Hello World !# defines window title
`

V V V V V V V V V V V V V V 

**.html**

```
<title>Hello World</title>
<!-- defines window title -->
```

## Expected Outcome
**.bagl**

`
-$ title = Hello World !# defines window title
`

V V V V V V V V V V V V V V 

**.html**

```
<title>Hello World</title><!-- defines window title -->
```