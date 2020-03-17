%%
%% LaTeX2e-Dokumentenklasse für BuB-Doku-Layout
%% möglichst schlank gehalten, wenige Abhängigkeiten
%% Stand 4.12.2017
%%
\NeedsTeXFormat{LaTeX2e}[1995/12/01]
\ProvidesClass{doku2018}[2017/12/04 LaTeX2e BuB New Layout]
\LoadClass[a4paper%
,10pt%
,twoside%
,twocolumn%
,openany%
,extrafontsizes%
]{memoir}

%%%%%%%%%%%%%%%%%
%%   Packages  %%
%%%%%%%%%%%%%%%%%


\RequirePackage{xparse}%
\RequirePackage{graphicx}%
\PassOptionsToPackage{%russian,%
	british,%
	ngerman}{babel}
\RequirePackage{babel}
\PassOptionsToPackage{T1}{fontenc}
\RequirePackage{fontenc}

\PassOptionsToPackage{utf8}{inputenc}
\RequirePackage{inputenc}

\RequirePackage{amsmath}
\RequirePackage{amsfonts}
\RequirePackage{euler}
\RequirePackage{booktabs}
\RequirePackage{eurosym}
\RequirePackage{float}


%%%%%%%%%%%%%%%%%%%%%%%%%%
%%   Lokale Variablen   %%
%%%%%%%%%%%%%%%%%%%%%%%%%%

\NewDocumentCommand\theacademy{}{Akademie}
\NewDocumentCommand\theyear{}{Jahr}
\NewDocumentCommand\theacademynumber{}{Nummer}

\NewDocumentCommand\thecoursetitle{}{Kurstitel}
\NewDocumentCommand\thecoursesubtitle{}{}
\NewDocumentCommand\thecourseshorttitle{}{Kurstitel (kurz)}
\NewDocumentCommand\thecoursenumber{}{Kursnummer}

\NewDocumentCommand\thelogofile{}{Titelbild-fehlt.png}
\NewDocumentCommand\thelogowidth{}{0.8\textwidth}

\NewDocumentCommand{\academy}{mmm}{
  \RenewDocumentCommand\theacademy{}{#1}
  \RenewDocumentCommand\theyear{}{#2}
  \RenewDocumentCommand\theacademynumber{}{#3}
}

\NewDocumentCommand\thecourselogo{}{}


\NewDocumentCommand{\course}{o O{} m m m}{
  \pagestyle{DSAcourse}%
  \IfNoValueTF{#1}%
    {\RenewDocumentCommand\thecourseshorttitle{}{#3}}%
    {\RenewDocumentCommand\thecourseshorttitle{}{#1}}%
  \RenewDocumentCommand\thecoursesubtitle{}{#2}%
  \RenewDocumentCommand\thecoursetitle{}{#3}%
  \RenewDocumentCommand\thecoursenumber{}{#4}%
  \RenewDocumentCommand\thecourselogo{}{#5}%
  \chapterstyle{DSAchapter}%
  \setcounter{chapter}{\the\numexpr#4-1\relax}%
  \chapter{#3}%
}

\newcommand{\authors}[1]{%
  {
    \leavevmode\phantom{\fontsize{12pt}{0pt}\selectfont\textbf{\thesection{}}}\hspace{10pt}
    \fontsize{9.8pt}{0pt}\selectfont\itshape#1%
  \par\nobreak\vspace*{10pt}}
  \@afterheading%
}

%%%%%%%%%%%%%%%%%%%%%
%%   Satzspiegel   %%
%%%%%%%%%%%%%%%%%%%%%

% rand bindung und außen
\setlrmarginsandblock{30mm}{20mm}{*}

% rand oben unten
\setulmarginsandblock{24mm}{25mm}{*}

% abstand zwischen den textspalten
\setcolsepandrule{5mm}{0pt}

\checkandfixthelayout

% einrückung der absätze
\setlength{\parindent}{6mm}

\makepagestyle{DSAcourse}

\NewDocumentCommand\headerfont{}{\fontsize{9.8pt}{0pt}\selectfont\scshape}

\makeevenhead{DSAcourse}{%
  \headerfont%
  Kurs \theacademynumber.\thecoursenumber~--~\thecourseshorttitle%
}{}{%
  \headerfont%
  \theacademy\ \theyear-\theacademynumber%
}
\makeoddhead{DSAcourse}{%
  \headerfont%
  \theacademy\ \theyear-\theacademynumber%
}{}{%
  \headerfont%
  Kurs \theacademynumber.\thecoursenumber~--~\thecourseshorttitle%
}

\makeheadrule{DSAcourse}{\textwidth}{0.5pt}
\makeevenfoot{DSAcourse}{\thepage}{}{}
\makeoddfoot{DSAcourse}{}{}{\thepage}

\copypagestyle{chapter}{plain}
\makeevenfoot{chapter}{\thepage}{}{}
\makeoddfoot{chapter}{}{}{\thepage}

\pagestyle{DSAcourse}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%   Layout von Kapiteln und Abschnitten   %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


\makechapterstyle{DSAchapter}{
\renewcommand*{\printchaptername}{}
\renewcommand*{\chapternamenum}{}
\renewcommand*{\printchapternum}{}
\renewcommand*{\afterchapternum}{}
\renewcommand*{\afterchaptertitle}{\vskip 2mm%
  \fontsize{14pt}{0pt}\selectfont\thecoursesubtitle%
  \begin{center}%
    \thecourselogo{}%
   \end{center}%
  
}
\renewcommand*{\chapnumfont}{\normalfont\huge\bfseries}
\renewcommand*{\chaptitlefont}{\centering\normalfont\fontsize{18pt}{0pt}\selectfont\bfseries}
\setlength{\beforechapskip}{0pt}
\setlength{\midchapskip}{0pt}
\setlength{\afterchapskip}{5ex}
}

\setsecnumdepth{subsubsection}
\renewcommand\thesection{\arabic{section}}
\setsecheadstyle{\flushleft\fontsize{12pt}{0pt}\selectfont\textbf}
\setsecindent{0pt}
\setaftersecskip{1pt}


\setsubsecheadstyle{\flushleft\fontsize{10pt}{0pt}\selectfont\textbf}
\setaftersubsecskip{1pt}

\setsubsubsecheadstyle{\flushleft\fontsize{10pt}{0pt}\selectfont\textbf}
\setaftersubsubsecskip{1pt}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%   Beschriftung von Abbildungen und Tabellen   %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\addto\captionsngerman{%
  % buchstaben sind teuer
\renewcommand{\figurename}{Abb.\!}%
\renewcommand{\tablename}{Tab.\!}%
}

\captionnamefont{\fontsize{9pt}{0pt}\selectfont\itshape}
\captiontitlefont{\fontsize{9pt}{0pt}\selectfont\itshape}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%   Französische Anführungszeichen mit deutschen Abständen   %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\PassOptionsToPackage{autostyle=once,german=guillemets}{csquotes}
\RequirePackage{csquotes}
\defineshorthand{"`}{\openautoquote}
\defineshorthand{"'}{\closeautoquote}



%%%%%%%%%%%%%%%%%%
%%   Fußnoten   %%
%%%%%%%%%%%%%%%%%%

\renewcommand*{\footnoterule}{%
\kern-3pt%
\hrule width 25mm height 0.75pt
\kern 2.6pt}

\renewcommand{\foottextfont}{\fontsize{8pt}{0pt}\selectfont}

%%%%%%%%%%%%%%%%%%
%%   Hyperref   %%
%%%%%%%%%%%%%%%%%%

\PassOptionsToPackage{hyphens}{url}

\RequirePackage{hyperref}
% umbrüche überall erlauben
\g@addto@macro\UrlBreaks{
  \do\a\do\b\do\c\do\d\do\e\do\f\do\g\do\h\do\i\do\j
  \do\k\do\l\do\m\do\n\do\o\do\p\do\q\do\r\do\s\do\t
  \do\u\do\v\do\w\do\x\do\y\do\z\do\&\do\1\do\2\do\3
  \do\4\do\5\do\6\do\7\do\8\do\9\do\0\do\/}
\urlstyle{same}


