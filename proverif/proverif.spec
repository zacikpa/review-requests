%global debug_package %{nil}

Summary: Cryptographic protocol verifier in the formal model
Name: proverif
Version: 2.04
Release: %autorelease
URL: https://bblanche.gitlabpages.inria.fr/%{name}
License: GPL-2.0-or-later
Source0: %{url}/%{name}%{version}.tar.gz

BuildRequires: glibc
BuildRequires: graphviz
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: m4
BuildRequires: gtk2-devel
BuildRequires: ocaml-lablgtk-devel

%description
ProVerif is an automatic cryptographic protocol verifier, in the formal
model (so called Dolev-Yao model). This protocol verifier is based
on a representation of the protocol by Horn clauses.

%prep
%autosetup -n %{name}%{version}

%build
./build

%check
./test

%install
install -vd                   %{buildroot}%{_bindir}
install -vp proverif          %{buildroot}%{_bindir}/
install -vp proverif_interact %{buildroot}%{_bindir}/
install -vp proveriftotex     %{buildroot}%{_bindir}/

%files
%{_bindir}/proverif
%{_bindir}/proverif_interact
%{_bindir}/proveriftotex
%license LICENSE
%doc README CHANGES

%changelog
%autochangelog
