function finderfeature
    cd ../
    tangleweave generators.pnw
    cd tests/steps
    tangleweave finderfeature.pnw
    cd ../
    behave features/finder.feature
end

function moverfeature
    cd ../
    Pweave -m mover.pnw
    Ptangle mover.pnw
    cd tests/steps
    Ptangle moverfeature.pnw
    Pweave -m moverfeature.pnw
    cd ../
    behave features/mover.feature
end

function copierfeature
    cd ../
    Pweave -m copier.pnw
    Ptangle copier.pnw
    cd tests/steps
    Ptangle copierfeature.pnw
    Pweave -m copierfeature.pnw
    cd ../
    behave features/copier.feature
end

function testall
    finderfeature
    moverfeature
end
