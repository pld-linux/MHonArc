Summary:	An Email-to-HTML converter
Summary(pl):	Konwerter Poczta->HTML
Name:		MHonArc
Version:	2.4.5
Release:	1
License:	GPL
Group:		Applications/Mail
Group(pl):	Aplikacje/Poczta
Vendor:		Earl Hood <ehood@medusa.acs.uci.edu>
Source0:	http://www.oac.uci.edu/indiv/ehood/tar/%{name}%{version}.tar.bz2
Patch0:		MHonArc-perl.patch.gz
Patch1:		MHonArc-FHS2.patch
URL:		http://www.oac.uci.edu/indiv/ehood/mhonarc.html
BuildRequires:	perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
install -d		$RPM_BUILD_ROOT%{_bindir}
install -d		$RPM_BUILD_ROOT%{_mandir}/man1
install -d		$RPM_BUILD_ROOT%{_datadir}/%{name}

install mhonarc		$RPM_BUILD_ROOT%{_bindir}
install mha-*		$RPM_BUILD_ROOT%{_bindir}
install man/*.1		$RPM_BUILD_ROOT%{_mandir}/man1
install lib/*		$RPM_BUILD_ROOT%{_datadir}/%{name}

gzip -9nf ACKNOWLG BUGS CHANGES RELNOTES \
	  $RPM_BUILD_ROOT%{_mandir}/man1/*.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc examples extras logo admin
%doc {ACKNOWLG,BUGS,CHANGES,RELNOTES}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/%{name}
