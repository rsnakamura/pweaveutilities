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
