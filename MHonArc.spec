Summary:     An Email-to-HTML converter
Summary(pl): Konwerter Poczta->HTML
Name:        MHonArc
Version:     2.3.3
Release:     1
Copyright:   GPL
Group:       Applications/Mail
Group(pl):   Aplikacje/Poczta
Vendor:      Earl Hood <ehood@medusa.acs.uci.edu>
Source:      %{name}%{version}.tar.gz
Patch:       MHonArc.perl.diff
URL:         http://www.oac.uci.edu/indiv/ehood/mhonarc.html
Icon:        monicon.gif
BuildArch:   noarch
BuildRoot:   /tmp/%{name}-%{version}-root

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
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,lib/MHonArc}

install mhonarc $RPM_BUILD_ROOT/usr/bin
install mha-dbedit $RPM_BUILD_ROOT/usr/bin
install mha-dbrecover $RPM_BUILD_ROOT/usr/bin
install lib/* $RPM_BUILD_ROOT/usr/lib/MHonArc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc doc examples extras logo ACKNOWLG BUGS CHANGES RELNOTES
%attr(755, root, root) /usr/bin/*
%attr(644, root, root, 755) /usr/lib/MHonArc/*

%changelog
* Sun Nov 29 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.3.3-1]
- added package Icon,
- modified pl translation.

* Thu Nov 05 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- added pl translation,
- instead sed commands is now simple patch.

* Sat Oct 30 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- initial RPM release
