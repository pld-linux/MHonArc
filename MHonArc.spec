Summary:	An Email-to-HTML converter
Summary(pl):	Konwerter Poczta->HTML
Name:		MHonArc
Version:	2.3.3
Release:	3
Copyright:	GPL
Group:		Applications/Mail
Group(pl):	Aplikacje/Poczta
Vendor:		Earl Hood <ehood@medusa.acs.uci.edu>
Source:		http://www.oac.uci.edu/indiv/ehood/tar/%{name}%{version}.tar.gz
Patch0:		MHonArc-perl.patch.gz
Patch1:		MHonArc-FHS2.patch
URL:		http://www.oac.uci.edu/indiv/ehood/mhonarc.html
Icon:		monicon.gif
BuildRequires:	perl
BuildArch:	noarch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
MHonArc is a Perl mail-to-HTML converter. MHonArc provides HTML mail
archiving with index, mail thread linking, etc; plus other capabilities
including support for MIME and powerful user customization features.
	    
%description -l pl
MHonArc to konwerter poczta->HTML napisany w perlu. MHonArc pozwala na
archiwizowanie poczty w postaci stron HTML z indeksowaniem wed³ug w±tku.
MHonArc wspiera MIME oraz ³atwo przystosowuje siê do wymagañ u¿ytkownika.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,share/MHonArc}

install mhonarc $RPM_BUILD_ROOT%{_bindir}
install mha-dbedit $RPM_BUILD_ROOT%{_bindir}
install mha-dbrecover $RPM_BUILD_ROOT%{_bindir}
install lib/* $RPM_BUILD_ROOT%{_datadir}/MHonArc

gzip -9nf ACKNOWLG BUGS CHANGES RELNOTES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc examples extras logo 
%doc {ACKNOWLG,BUGS,CHANGES,RELNOTES}.gz

%attr(755,root,root) %{_bindir}/*
%{_datadir}/MHonArc
