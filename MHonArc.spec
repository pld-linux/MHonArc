%include	/usr/lib/rpm/macros.perl
Summary:	An Email-to-HTML converter
Summary(pl):	Konwerter Poczta->HTML
Name:		MHonArc
Version:	2.6.10
Release:	1
License:	GPL
Vendor:		Earl Hood <ehood@medusa.acs.uci.edu>
Group:		Applications/Mail
Source0:	http://www.mhonarc.org/tar/%{name}-%{version}.tar.bz2
# Source0-md5:	337dfa5660fa158e5a4e3fd74b4c2ec1
Patch0:		%{name}-FHS2.patch
Patch1:		%{name}-DESTDIR.aptch
URL:		http://www.mhonarc.org/
BuildRequires:	perl
Requires:	perl-Unicode-MapUTF8
Requires:	perl-Unicode-String
Requires:	perl-modules >= 5.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MHonArc is a Perl mail-to-HTML converter. MHonArc provides HTML mail
archiving with index, mail thread linking, etc; plus other
capabilities including support for MIME and powerful user
customization features.

%description -l pl
MHonArc to konwerter poczta->HTML napisany w perlu. MHonArc pozwala na
archiwizowanie poczty w postaci stron HTML z indeksowaniem wed³ug
w±tku. MHonArc wspiera MIME oraz ³atwo przystosowuje siê do wymagañ
u¿ytkownika.

%prep
%setup -q
perl -p -i -e 's|# ?!/usr/local/bin/perl|#!/usr/bin/perl|' `find . -type f`
%patch0 -p1
%patch1 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/%{name}/MHonArc/{Char,CharEnt,UTF8}}

install mhonarc mha-dbedit mha-dbrecover mha-decode  $RPM_BUILD_ROOT%{_bindir}

install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

install lib/*.pl $RPM_BUILD_ROOT%{_datadir}/%{name}
install lib/MHonArc/*.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/MHonArc
install lib/MHonArc/Char/*.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/MHonArc/Char
install lib/MHonArc/CharEnt/*.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/MHonArc/CharEnt
install lib/MHonArc/UTF8/*.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/MHonArc/UTF8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc examples extras logo admin ACKNOWLG BUGS CHANGES RELNOTES
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/*
