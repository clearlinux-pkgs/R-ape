#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ape
Version  : 5.3
Release  : 28
URL      : https://cran.r-project.org/src/contrib/ape_5.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ape_5.3.tar.gz
Summary  : Analyses of Phylogenetics and Evolution
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-ape-lib = %{version}-%{release}
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
No detailed description available

%package lib
Summary: lib components for the R-ape package.
Group: Libraries

%description lib
lib components for the R-ape package.


%prep
%setup -q -c -n ape

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571796137

%install
export SOURCE_DATE_EPOCH=1571796137
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ape
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ape
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ape
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ape || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ape/CITATION
/usr/lib64/R/library/ape/DESCRIPTION
/usr/lib64/R/library/ape/INDEX
/usr/lib64/R/library/ape/Meta/Rd.rds
/usr/lib64/R/library/ape/Meta/data.rds
/usr/lib64/R/library/ape/Meta/features.rds
/usr/lib64/R/library/ape/Meta/hsearch.rds
/usr/lib64/R/library/ape/Meta/links.rds
/usr/lib64/R/library/ape/Meta/nsInfo.rds
/usr/lib64/R/library/ape/Meta/package.rds
/usr/lib64/R/library/ape/Meta/vignette.rds
/usr/lib64/R/library/ape/NAMESPACE
/usr/lib64/R/library/ape/NEWS
/usr/lib64/R/library/ape/R/ape
/usr/lib64/R/library/ape/R/ape.rdb
/usr/lib64/R/library/ape/R/ape.rdx
/usr/lib64/R/library/ape/data/HP.links.rda
/usr/lib64/R/library/ape/data/bird.families.rda
/usr/lib64/R/library/ape/data/bird.orders.rda
/usr/lib64/R/library/ape/data/carnivora.csv.gz
/usr/lib64/R/library/ape/data/chiroptera.rda
/usr/lib64/R/library/ape/data/cynipids.rda
/usr/lib64/R/library/ape/data/gopher.D.rda
/usr/lib64/R/library/ape/data/hivtree.newick.rda
/usr/lib64/R/library/ape/data/hivtree.table.txt.gz
/usr/lib64/R/library/ape/data/lice.D.rda
/usr/lib64/R/library/ape/data/lmorigin.ex1.rda
/usr/lib64/R/library/ape/data/lmorigin.ex2.rda
/usr/lib64/R/library/ape/data/mat3.RData
/usr/lib64/R/library/ape/data/mat5M3ID.RData
/usr/lib64/R/library/ape/data/mat5Mrand.RData
/usr/lib64/R/library/ape/data/woodmouse.rda
/usr/lib64/R/library/ape/doc/MoranI.R
/usr/lib64/R/library/ape/doc/MoranI.Rnw
/usr/lib64/R/library/ape/doc/MoranI.pdf
/usr/lib64/R/library/ape/doc/index.html
/usr/lib64/R/library/ape/help/AnIndex
/usr/lib64/R/library/ape/help/aliases.rds
/usr/lib64/R/library/ape/help/ape.rdb
/usr/lib64/R/library/ape/help/ape.rdx
/usr/lib64/R/library/ape/help/paths.rds
/usr/lib64/R/library/ape/html/00Index.html
/usr/lib64/R/library/ape/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/ape/libs/ape.so
/usr/lib64/R/library/ape/libs/ape.so.avx2
/usr/lib64/R/library/ape/libs/ape.so.avx512
