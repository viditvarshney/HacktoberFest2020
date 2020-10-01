class Disk {
    var name: String
    
    init(_ name: String) {
        self.name = name
    }
}

class Peg: Printable {
    var name: String
    
    // Disks on peg, ordered from bottom to top
    var disks: Disk[]
    
    var diskCount: Int { return disks.count }
    
    var description: String {
        let diskNames = disks.map { $0.name }
        let diskNamesString = ", ".join(diskNames)
        return "\(name): \(diskNamesString)"
    }
    
    init(name: String, disks: Disk[]) {
        self.name = name
        self.disks = disks
    }
    
    convenience init(name: String) {
        self.init(name: name, disks: Array<Disk>())
    }
    
    func addDisk(disk: Disk) {
        disks.append(disk)
    }
    
    func removeTopDisk() -> Disk {
        return disks.removeLast()
    }
}

struct Move: Printable {
    var fromPeg: Peg
    var toPeg: Peg
    
    var description: String {
        return "\(fromPeg.name) -> \(toPeg.name)"
    }
    
    init(fromPeg: Peg, toPeg: Peg) {
        self.fromPeg = fromPeg
        self.toPeg = toPeg
    }
    
    func execute() -> Disk {
        let disk = fromPeg.removeTopDisk()
        toPeg.addDisk(disk)
        return disk
    }
}

struct HanoiSolver {
    
    // Return sequence of moves needed to move all disks from one peg to another,
    // using a third as intermediary
    
    func moveAllDisksFromPeg(fromPeg: Peg, toPeg: Peg, otherPeg: Peg) -> Move[] {
        return moveNumberOfDisks(fromPeg.diskCount,
            fromPeg:  fromPeg,
            toPeg:    toPeg,
            otherPeg: otherPeg)
    }
    
    // Calculate sequence of moves needed to move specified number of
    // disks from one peg to another, using a third peg as intermediary.
    //
    // Basic algorithm is:
    //
    // 1. Use this algorithm to move the top (n - 1) disks to the third peg
    // 2. Move the bottom disk to the destination peg
    // 3. Use this algorithm to move the (n - 1) disks from the third peg to the destination peg
    
    func moveNumberOfDisks(count: Int, fromPeg: Peg, toPeg: Peg, otherPeg: Peg) -> Move[] {
        var moves = Array<Move>()
        if count >= 1 {
            moves += moveNumberOfDisks(count - 1,
                fromPeg:  fromPeg,
                toPeg:    otherPeg,
                otherPeg: toPeg)
            
            moves += Move(fromPeg: fromPeg, toPeg: toPeg)
            
            moves += moveNumberOfDisks(count - 1,
                fromPeg:  otherPeg,
                toPeg:    toPeg,
                otherPeg: fromPeg)
        }
        return moves;
    }
}

// Disks ordered from bottom to top
let disks = [
    Disk("XLarge"),
    Disk("Large"),
    Disk("Medium"),
    Disk("Small"),
    Disk("Tiny")]
let pegA = Peg(name: "A", disks: disks)
let pegB = Peg(name: "B")
let pegC = Peg(name: "C")

println("Start:")
println(pegA.description)
println(pegB.description)
println(pegC.description)
println()

// Create solver and generate the sequence of moves needed
let moves = HanoiSolver().moveAllDisksFromPeg(pegA, toPeg: pegC, otherPeg: pegB)

// Apply the moves
println("Number of moves: \(moves.count)")
for move in moves {
    println(move.description)
    move.execute()
}

println("\nFinish:")
println(pegA.description)
println(pegB.description)
println(pegC.description)
