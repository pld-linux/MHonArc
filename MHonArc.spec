Summary:	An Email-to-HTML converter
Summary(pl.UTF-8):	Konwerter Poczta->HTML
Name:		MHonArc
Version:	2.6.19
Release:	1
License:	GPL v2+
Group:		Applications/Mail
Source0:	https://www.mhonarc.org/release/MHonArc/tar/%{name}-%{version}.tar.bz2
# Source0-md5:	6e74712a6da370c8c63b5bde7573f48f
Patch0:		%{name}-FHS2.patch
URL:		https://www.mhonarc.org/
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	sed >= 4.0
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

%description -l pl.UTF-8
MHonArc to konwerter poczta->HTML napisany w Perlu. MHonArc pozwala na
archiwizowanie poczty w postaci stron HTML z indeksowaniem według
wątku. MHonArc obsługuje MIME oraz łatwo przystosowuje się do wymagań
użytkownika.

%prep
%setup -q
%patch -P0 -p1

# some files have /usr/local/bin/perl or /net/nf/bin/perl
%{__sed} -i -e '1s,^#!.*bin/perl5\?,#!%{__perl},' $(grep -rl '^#!.*/bin/perl' .)

%build
%{__perl} Makefile.PL

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__perl} install.me \
	-batch \
	-nodoc \
	-manpath=%{_mandir} \
	-binpath=%{_bindir} \
	-libpath=%{_datadir}/%{name} \
	-root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNOWLG BUGS CHANGES README.txt RELNOTES TODO admin doc examples extras logo
%attr(755,root,root) %{_bindir}/mha-dbedit
%attr(755,root,root) %{_bindir}/mha-dbrecover
%attr(755,root,root) %{_bindir}/mha-decode
%attr(755,root,root) %{_bindir}/mhonarc
%{_datadir}/%{name}
%{_mandir}/man1/mha-dbedit.1*
%{_mandir}/man1/mha-dbrecover.1*
%{_mandir}/man1/mha-decode.1*
%{_mandir}/man1/mhonarc.1*
