%include	/usr/lib/rpm/macros.perl
Summary:	An Email-to-HTML converter
Summary(pl):	Konwerter Poczta->HTML
Name:		MHonArc
Version:	2.5.3
Release:	1
License:	GPL
Vendor:		Earl Hood <ehood@medusa.acs.uci.edu>
Group:		Applications/Mail
Source0:	http://www.mhonarc.org/tar/%{name}%{version}.tar.bz2
Patch0:		%{name}-FHS2.patch
Patch1:		%{name}-DESTDIR.aptch
URL:		http://www.mhonarc.org/
BuildRequires:	perl
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
%setup -q -n %{name}%{version}
perl -p -i -e 's|# ?!/usr/local/bin/perl|#!/usr/bin/perl|' `find . -type f`
%patch0 -p1
%patch1 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/%{name}/MHonArc/CharEnt}

install mhonarc mha-dbedit mha-dbrecover mha-decode  $RPM_BUILD_ROOT%{_bindir}

install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

install lib/*.pl $RPM_BUILD_ROOT%{_datadir}/%{name}
install lib/MHonArc/*.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/MHonArc
install lib/MHonArc/CharEnt*.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/MHonArc/CharEnt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc examples extras logo admin ACKNOWLG BUGS CHANGES RELNOTES
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/*
